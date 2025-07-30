import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def fetch_page(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def scrape_content(self, html):
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        return text



