# main.py

import logging
from scraping_amazon.data_handler import read_links, save_to_csv
from scraping_amazon.scraper import fetch_product_details

# Configure logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    links = read_links('links.txt')
    if not links:
        logging.error("No links found in links.txt. Exiting...")
        return

    all_product_details = []
    for link in links:
        details = fetch_product_details(link)
        if details:
            all_product_details.append(details)

    if all_product_details:
        save_to_csv(all_product_details)

if __name__ == '__main__':
    main()
