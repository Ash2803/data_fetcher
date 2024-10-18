import requests
import os
import logging

from dotenv import load_dotenv

class ProductAPI:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("BASE_URL")

    def get_products(self) -> list[dict]:
        """
        Fetches products from the API using a GET request.

        :return: A list of dictionaries containing product data.
        :raises requests.exceptions.RequestException: If the request fails.
        """
        logger = logging.getLogger(__name__)
        url = self.base_url
        limit = 194
        try:
            params = {
                "limit": limit
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json().get("products", {})
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching products: {e}")
            raise
