from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

URL = "https://devpost.com/hackathons?pages=6"
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
            image_link = hackathon.select_one('img')
            title = hackathon.select_one('h3')
            hackathon_link = hackathon.select_one('a.tile-anchor')
            prize = hackathon.select_one('span.prize-amount')
            participants = hackathon.select_one('div.participants')
            days_left = hackathon.select_one('.status-label')
            submission_period = hackathon.select_one('.submission-period')
            organization = hackathon.select_one('.host-label')
            themes = hackathon.select('.theme-label')

            data = {
                "img" : image_link['src'] if image_link else None,
                "title" : title.get_text(strip=True) if title else None,
                "link" : hackathon_link['href'] if hackathon_link else None,
                "organization" : organization.get_text(strip=True) if organization else None,
                "prize" : prize.get_text(strip=True) if prize else None,
                "participants" : participants.get_text(strip=True) if participants else None,
                "submission period" : submission_period.get_text(strip=True) if submission_period else None,
                "days left" : days_left.get_text(strip=True) if days_left else None,
                "themes" : [theme.get_text(strip=True) for theme in themes] if themes else []
            }
            fetched_hackathons.append(data)
        print(fetched_hackathons)
    except Exception as error:
        # Exception to catch errors
        print(error)
        raise error

fetch_data(URL)
