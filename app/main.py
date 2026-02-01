from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

URL = "https://devpost.com/hackathons?pages=5"
def fetch_data(url):
    try:
        # initializing selenium chrome service
        service = Service(ChromeDriverManager().install())

        # initializing browser (chrome)
        browser = webdriver.Chrome(service=service)
        
        # Load dynamic page
        browser.get(url)
        # Explicitly wait for dynamic page to load (hackathons container)
        WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "hackathon-tile")))

        # Load html content
        html_body = browser.page_source
        # Starting our soup instance, soup will extract required fields from the returned html
        soup = BeautifulSoup(html_body, "html.parser")
        fetched_hackathons = []

        # Fetch hackathons details with soup
        hackathons = soup.select('.hackathon-tile')
        print(len(hackathons))
        for hackathon in hackathons:
            title = hackathon.select_one('h3')
            print(title)

        # print(soup)
    except Exception as error:
        # Exception to catch errors
        print(error)
        raise error

fetch_data(URL)
