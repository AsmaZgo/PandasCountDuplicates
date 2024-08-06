import pandas as pd
from typing import Dict, List


def count_duplicates(df: pd.DataFrame, col_list: List[str]) -> Dict[str, pd.DataFrame]:
    """
        Check and count the duplicates in the dataframe for a predefined list of columns.

        Args:
        df: The input dataframe.
        col_list: List of columns to check for duplicates.

        Returns:
        A dictionary composed of count : the number of cases where duplicates occur in the dataframe and samples: a dataframe with rows that have duplicate values in the specified columns and their counts.
    """

    # Verify if a given column in the list isn't in the dataframe
    for col in col_list:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' does not exist in the dataframe! Please verify your input.")
    # Group the data based on the column list and count the values occurrences
    df_count_values_occurrence = df.groupby(col_list).size().reset_index(name='num_occurrences')
    # Find the duplicates that have a higher than 1 occurrence
    duplicates = df_count_values_occurrence.where(df_count_values_occurrence['num_occurrences'] > 1).dropna()
    duplicates['num_occurrences'] = duplicates['num_occurrences'].astype(int)
    return {"count": len(duplicates.index),
            "samples": duplicates}
