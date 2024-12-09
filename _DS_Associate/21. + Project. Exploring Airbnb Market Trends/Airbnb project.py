# Import necessary packages
import pandas as pd
import numpy as np
import os

# 1. Read all data files
# Read csv:
prices = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'airbnb_price.csv'))
prices.info()

# Read the TSV file using read_csv with tab delimiter and handle bad lines
review = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'airbnb_last_review.tsv'), delimiter='\t', on_bad_lines='skip')
review.info()

# Read the XLS file using read_excel
room = pd.read_excel(os.path.join(os.path.dirname(__file__), 'data', 'airbnb_room_type.xlsx')) 
room.info()
room['room_type'].value_counts()

# 2. Find the first and last review dates

# Convert the 'last_review' column to datetime
review['last_review'] = pd.to_datetime(review['last_review'])

first_reviewed = review['last_review'].min()
last_reviewed = review['last_review'].max()

# Print the first and last review dates 
print(first_reviewed)
print(last_reviewed)

# 3. Find the number of private rooms
room['room_type'] = room['room_type'].str.lower()
room["room_type"].value_counts()
private_room_count = room[room['room_type'] == 'private room']['room_type'].value_counts()
print(private_room_count)

# 4. Find the average price of listings
prices['price'] = prices['price'].str.replace(' dollars', '').astype(float)
duplicates = prices.duplicated().sum()
price_avg = prices['price'].mean().round(2)

# DataFrame with results
review_dates = pd.DataFrame({
    'first_reviewed': [first_reviewed],
    'last_reviewed': [last_reviewed],
    'nb_private_rooms': [private_room_count.values[0]],
    'avg_price': [price_avg]
}, index=[0])

print(review_dates)