# Pandas Count Duplicates

A tool that given a list of columns, checks in a dataset for duplicates, counts them and display a report with the duplicated values and their counts.

## Usage

Run the tool from the main file using the following command:
```
python main.py <dataset path> <columns list>
```

e.g:
```
python main.py "tests/files/input.csv" "col_1" "col_2"
```

Expected results (the duplicates report): 

  1. col_1, col_2, num_occurrences
  2. A, a, 2


2024-08-07 10:58:29,298 - INFO - Number of duplicate cases: 1

## Libraries 
- Pandas
- Python 3
