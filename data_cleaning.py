import pandas as pd

# Load the dataset
df = pd.read_csv("titanic.csv")

# Display first 5 rows
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())
# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Handle missing values

# Fill missing Age values with the median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with the most frequent value
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Cabin has many missing values, so drop the column
df = df.drop(columns=["Cabin"])

# Check missing values again
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())
# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())
# Check data types
print("\nData Types:")
print(df.dtypes)
# Check unique values for categorical columns

print("\nUnique values in Sex:")
print(df["Sex"].unique())

print("\nUnique values in Embarked:")
print(df["Embarked"].unique())

print("\nUnique values in Pclass:")
print(df["Pclass"].unique())
# Final verification

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFinal Missing Values:")
print(df.isnull().sum())

print("\nFinal Duplicate Records:")
print(df.duplicated().sum())

# Save cleaned dataset
df.to_csv("titanic_cleaned.csv", index=False)

print("\nCleaned dataset saved as titanic_cleaned.csv")