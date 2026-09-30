# SWYNEX - Data Cleaning & Preparation

## Task 1: Data Cleaning & Preparation

This project focuses on cleaning and preparing the Titanic dataset for data analysis.

## Dataset

Dataset: Titanic Dataset

Original dataset:
- Rows: 891
- Columns: 12

## Data Cleaning Performed

### 1. Missing Values
- Age had 177 missing values.
- Missing Age values were filled using the median.
- Embarked had 2 missing values.
- Missing Embarked values were filled using the mode.
- Cabin had 687 missing values, so the Cabin column was removed.

### 2. Duplicate Records
- Duplicate records were checked.
- Total duplicate records found: 0.

### 3. Data Types
Data types were checked for all columns and were found to be appropriate for the dataset.

### 4. Inconsistent Values
Categorical values were checked:
- Sex: male, female
- Embarked: S, C, Q
- Pclass: 1, 2, 3

No obvious inconsistent values were found.

## Final Dataset

After cleaning:
- Missing values: 0
- Duplicate records: 0
- Final rows: 891
- Final columns: 11

## Tools Used

- Python
- Pandas
- CSV Dataset

## Files

- `titanic.csv` - Original dataset
- `data_cleaning.py` - Python data cleaning script
- `titanic_cleaned.csv` - Cleaned dataset