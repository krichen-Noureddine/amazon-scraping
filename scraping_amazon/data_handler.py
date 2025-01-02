# data_handler.py

import csv
import os
import logging

logger = logging.getLogger(__name__)

def read_links(file_path='links.txt'):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        logger.error(f"File {file_path} not found.")
        return []

def save_to_csv(all_product_details, filename='product_details.csv'):
    try:
        data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        file_path = os.path.join(data_dir, filename)
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(all_product_details[0].keys())
            for product_details in all_product_details:
                writer.writerow(product_details.values())
        logger.info(f"Data saved to {file_path}")
    except Exception as e:
        logger.error(f"Error saving data to CSV: {e}")
