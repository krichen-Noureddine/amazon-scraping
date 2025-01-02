# utils.py

import os
import logging
import requests

logger = logging.getLogger(__name__)

def save_image(image_url, product_title):
    try:
        logger.info(f"Downloading image from URL: {image_url}")
        image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../images')
        
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
        
        file_name = f"{product_title[:50].replace(' ', '_').replace('/', '_')}.jpg"
        image_path = os.path.join(image_dir, file_name)
        
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(image_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            logger.info(f"Image saved at {image_path}")
            return image_path
        else:
            logger.error(f"Failed to download image: {response.status_code}")
            return None
    except Exception as e:
        logger.error(f"Error saving image: {e}")
        return None
