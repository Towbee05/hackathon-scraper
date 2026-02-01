from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from typing import List, TypedDict
import json
import sys

class Hackathon(TypedDict):
    img : str | None
    title : str | None
    link : str | None
    organization : str | None
    prize : str
    participants : str | None
    submission_period : str | None
    days_left : str | None
    themes : List[str] | None

def main():
    URL = "https://devpost.com/hackathons?page=1"
    html = fetch_data(URL, 20)
    data = parse_html_into_dict(html=html)
    try:
        feed_data_into_json_file(data, "hackathons.json")
        print("Your data now exists in json file!!!!!")
        sys.exit(1)
    except Exception as error:
        print(error)
        sys.exit(0)

def fetch_data(url: str, timeout: int=20) -> str:
    # initializing selenium chrome service
    service = Service(ChromeDriverManager().install())
    # initializing browser (chrome)
    browser = webdriver.Chrome(service=service)
    
    # Load dynamic page
    try:
        browser.get(url)
        # Explicitly wait for dynamic page to load (hackathons container)
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "hackathon-tile")))
        # Load html content
        html_body = browser.page_source
        return html_body
    finally:
        browser.quit()

def parse_html_into_dict(html: str) -> List[Hackathon]:
    # Starting our soup instance, soup will extract required fields from the returned html
    soup = BeautifulSoup(html, "html.parser")
    fetched_hackathons = []
    # Fetch hackathons details with soup
    hackathons = soup.select('.hackathon-tile')
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
            "title" : retrieve_text_or_none(title),
            "link" : hackathon_link['href'] if hackathon_link else None,
            "organization" : retrieve_text_or_none(organization),
            "prize" : prize.get_text(strip=True) if prize else "$0.0",
            "participants" : retrieve_text_or_none(participants),
            "submission_period" : retrieve_text_or_none(submission_period),
            "days_left" : retrieve_text_or_none(days_left),
            "themes" : [retrieve_text_or_none(theme) for theme in themes] if themes else None
        }
        fetched_hackathons.append(data)
    return fetched_hackathons

# Function to create json file of fetched hackathons
def feed_data_into_json_file(data, filename):
    with open(filename, "w", encoding="utf-8") as file_dump:
        json.dump(data, file_dump, ensure_ascii= False)

def retrieve_text_or_none(text): 
    return text.get_text(strip=True) if text else None # type: ignore


if __name__ == "__main__":
    main()
