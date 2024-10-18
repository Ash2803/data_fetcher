import os
import pandas as pd


def calculate_final_price(product) -> float:
    """
    Calculates the final price of a product after applying the discount.

    :param product: A dictionary containing product data.
    :return: The final price of the product.
    """
    price = product["price"]
    discount = product["discountPercentage"]
    final_price = price - (price * discount / 100)
    return round(final_price, 2)


def save_products_with_final_price(products: list[dict]) -> None:
    """
    Saves the product data with final prices to a parquet file.

    :param products: A list of dictionaries containing product data.
    """
    file_path = "./data/actual_data/product_prices_calculated_actual.parquet"

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    product_data = []

    for product in products:
        final_price = calculate_final_price(product)
        product_data.append({
            "id": product["id"],
            "title": product["title"],
            "price": product["price"],
            "discountPercentage": product["discountPercentage"],
            "final_price": final_price
        })

    df = pd.DataFrame(product_data)
    df.to_parquet(file_path, index=False)
    # it's not a best practice to use print() but I did it for this task
    print(f"Actual data saved to {file_path}")
