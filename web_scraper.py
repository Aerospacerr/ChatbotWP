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


if __name__ == "__main__":
    scraper = WebScraper()
    url = "example_url"
    html_content = scraper.fetch_page(url)
    if html_content:
        text_content = scraper.scrape_content(html_content)
        print("Fetched Content:", text_content)
    else:
        print("Failed to fetch the page.")
