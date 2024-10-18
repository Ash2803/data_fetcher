import pandas as pd

from client.products_client import ProductAPI
from src.product_data_analyzer import load_expected_data, find_most_expensive_product, find_missing_products, \
    count_matching_prices
from src.product_data_generation import save_products_with_final_price


def main():
    product_api = ProductAPI()
    products = product_api.get_products()
    save_products_with_final_price(products=products)
    actual_data_file_path = "./data/product_prices_calculated.parquet"
    expected_data_file_path = "./data/actual_data/product_prices_calculated_actual.parquet"
    expected_data = load_expected_data(actual_data_file_path)
    actual_data = pd.read_parquet(expected_data_file_path)
    missing_products = find_missing_products(actual_data=actual_data, expected_data=expected_data)
    print(missing_products)
    matching_prices = count_matching_prices(actual_data=actual_data, expected_data=expected_data)
    print(matching_prices)
    most_expensive_product = find_most_expensive_product(actual_data)
    print("Most expensive product based on actual data:", most_expensive_product)
    # it's not a best practice to use print() but I did it for this task

if __name__ == "__main__":
    main()
