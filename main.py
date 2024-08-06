import logging
from builtins import FileNotFoundError
import pandas as pd
from IPython.display import display
from typing import List
from processing.data_transformer import count_duplicates
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main(df: pd.DataFrame, col_list: List[str]) -> None:
    """
    Main function.

    Args:
    df: The input dataframe.
    col_list: List of columns to check for duplicates.
    """
    # Input checks
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The first argument must be a pandas DataFrame.")
    if not all(isinstance(col, str) for col in col_list):
        raise TypeError("The column list must contain strings only.")

    try:
        # Count duplicates in the specified columns
        results = count_duplicates(df, col_list)
        display(results['samples'])
        logging.info(f"Number of duplicate cases: {results['count']}")
    except ValueError as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Load a dataset from a CSV file and check for duplicates.')
    parser.add_argument('csv_path', type=str, help='Path to the CSV file.')
    parser.add_argument('columns', type=str, nargs='+', help='List of columns to check for duplicates.')

    args = parser.parse_args()

    try:
        df_1 = pd.read_csv(args.csv_path)
    except FileNotFoundError:
        logging.critical(f"File not found: {args.csv_path}")
        exit(1)
    except Exception as e:
        logging.critical(f"An error occurred while reading the CSV file: {e}")
        exit(1)

    # Pass the dataframe and column list to the main function
    main(df_1, args.columns)
