#00_clean.py

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Create folders if they don't exist
os.makedirs("data/clean", exist_ok=True)

# Read data
# raw_df = pd.read_csv("https://osf.io/z7vy6/download")

# Freeing memory
# df = raw_df.assign (nnights = 1) #saves it as a different data frame. Creating a new column 'nnights' and assigning the value 1 to all rows
# del raw_df #deleting the raw_data dataframe to free up memory

df.columns # checking dataframe columns
df['property_type'].unique() # checking unique values in 'property_type' column
df.shape

# Filtering observations 

df.loc [df['property_type'] == 'Apartment']
print (df['review_scores_rating'].isnull().sum())

df['property_type'].value_counts(dropna=False)

df = df[df['property_type'] == 'Apartment']

df.filter (regex = 'price')
df = df.rename (columns
    ={
        'price': 'd_price',
        'monthly_price': 'm_price',
        'weekly_price': 'w_price'})


# Cleaning d_price variable
# df['d_price'] = df['d_price'].str.replace('[\$,]', '', regex=True).str.strip()

# Convert to numeric
# df['d_price'] = pd.to_numeric(df['d_price'], errors='coerce')

# Create a new column for d_price bins
df['price_bin'] = pd.qcut(df['d_price'], q=10)
df[['property_type', 'd_price', 'm_price', 'w_price', 'price_bin']].head(20)

# Creating a price category label
df['price_category'] = ''
for i in range(len(df)):
    price = df.iloc[i]['d_price']  # use iloc instead of loc
    if price < 67:
        df.iloc[i, df.columns.get_loc('price_category')] = 'Low'
    elif price < 175:
        df.iloc[i, df.columns.get_loc('price_category')] = 'Medium'
    else:
        df.iloc[i, df.columns.get_loc('price_category')] = 'High'

review_category = []

for reviews in df['number_of_reviews']:
    if reviews == 0:
        review_category.append('No Reviews')
    elif reviews <= 10:  
        review_category.append('Few Reviews')
    elif reviews <= 40:
        review_category.append('Moderate Reviews')
    else:
        review_category.append('Many Reviews')

df['review_category'] = review_category

# Summary statistics
print(df['d_price'].describe())
print(df['number_of_reviews'].describe())

# Histogram of d_price
plt.figure(figsize=(8,5))
sns.boxplot(x='review_category', y='d_price', data=df, palette='coolwarm')
plt.yscale('log') 
plt.title('Price Distribution by Review Category (Log Scale)')
plt.xlabel('Review Category')
plt.ylabel('Price (log)')
plt.show()


# Save cleaned data
df.to_csv("data/clean/airbnb_clean.csv", index=False)

print("Cleaned data saved as data/clean/airbnb_clean.csv")