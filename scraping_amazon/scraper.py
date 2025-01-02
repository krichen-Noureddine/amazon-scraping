# scraper.py
import requests
from bs4 import BeautifulSoup
from scraping_amazon.utils import save_image
from scraping_amazon.config import HEADERS, COOKIES
import logging

logger = logging.getLogger(__name__)

def fetch_product_details(url):
    try:
        logger.info(f"Fetching details for URL: {url}")
        response = requests.get(url, headers=HEADERS, cookies=COOKIES)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')

            # Extraction des données
            product_details = {}
            title = soup.select_one('span#productTitle')
            product_details['Title'] = title.text.strip() if title else "Not found"
            
            # Price extraction
            whole_price = soup.select_one('span.a-price-whole')
            fraction_price = soup.select_one('span.a-price-fraction')
            currency_symbol = soup.select_one('span.a-price-symbol')

            if whole_price and fraction_price and currency_symbol:
                product_details['Price'] = f"{whole_price.text.strip()},{fraction_price.text.strip()} {currency_symbol.text.strip()}"
            else:
                product_details['Price'] = "Not available"
            
            # More details
            image = soup.select_one('img#landingImage')
            product_details['Image'] = save_image(image['src'], product_details['Title']) if image else "No image found"
            
            return product_details
        else:
            logger.error(f"Failed to fetch URL {url}: {response.status_code}")
            return None
    except Exception as e:
        logger.error(f"Error fetching URL {url}: {e}")
        return None
