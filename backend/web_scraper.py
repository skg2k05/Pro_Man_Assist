import requests
from bs4 import BeautifulSoup

def scrape_website(url, max_chars=3000):
    """
    Scrapes and cleans text content from a website.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "header", "footer", "nav"]):
            tag.decompose()

        text = " ".join(soup.stripped_strings)
        return text[:max_chars]
    except Exception as e:
        return f"[Error fetching website: {e}]"
import requests
from bs4 import BeautifulSoup

def scrape_website(url, max_chars=3000):
    """
    Scrapes and cleans text content from a website.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "header", "footer", "nav"]):
            tag.decompose()

        text = " ".join(soup.stripped_strings)
        return text[:max_chars]
    except Exception as e:
        return f"[Error fetching website: {e}]"
