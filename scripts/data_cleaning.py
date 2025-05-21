import pandas as pd

# Load your data into a DataFrame
# Replace 'your_data.csv' with the actual path to your data file
df = pd.read_csv('data/benin-malanville.csv')

# Basic Overview
df.info()
df.describe(include='all')

# Missing Values
missing = df.isna().sum()
missing_percent = (missing / len(df)) * 100
print(missing_percent[missing_percent > 5])  # >5% nulls

from scipy.stats import zscore

# Target columns
target_cols = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']
z_scores = df[target_cols].apply(zscore)
outliers = (z_scores.abs() > 3).any(axis=1)

# Flagging
df['Outlier'] = outliers

# Impute or Drop
for col in target_cols:
    df[col] = df[col].fillna(df[col].median())

    # Save cleaned CSV
df_cleaned = df[~df['Outlier']]
df_cleaned.to_csv('/content/benin-malanville.csv', index=False)
