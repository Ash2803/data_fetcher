import pandas as pd

def load_expected_data(file_path: str) -> pd.DataFrame:
    """
    Loads expected product data from a parquet file.

    :param file_path: Path to the parquet file containing expected data.
    :return: A DataFrame with expected product data.
    """
    return pd.read_parquet(file_path)

def find_most_expensive_product(products: pd.DataFrame) -> pd.Series:
    """
    Finds the most expensive product based on actual data.

    :param products: DataFrame containing actual product data.
    :return: A Series containing the details of the most expensive product.
    """
    return products.loc[products["final_price"].idxmax()]

def find_missing_products(actual_data: pd.DataFrame, expected_data: pd.DataFrame) -> pd.DataFrame:
    """
    Finds products that are missing in the expected data when compared to actual data.

    :param actual_data: DataFrame containing actual product data.
    :param expected_data: DataFrame containing expected product data.
    :return: A DataFrame with products that are missing in the expected data.
    """
    missing_products = actual_data[~actual_data['id'].isin(expected_data['id'])]
    return missing_products

def count_matching_prices(actual_data: pd.DataFrame, expected_data: pd.DataFrame) -> int:
    """
    Counts the number of rows where the final price in the expected data matches the calculated price from the actual data.

    :param actual_data: DataFrame containing actual product data.
    :param expected_data: DataFrame containing expected product data.
    :return: The number of rows where the final prices match.
    """
    merged_data = pd.merge(actual_data, expected_data, on="id", suffixes=("_actual", "_expected"))
    return (merged_data["final_price_actual"] == merged_data["final_price_expected"]).sum()
