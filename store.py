import scraper as  sc
import pandas as pd
import tabulate as tb

df = pd.read_csv('output.csv')

price = df['Price'].str.replace('$', '').astype(float)

category = input('Choose your category between Phones and Computers: ').capitalize()

min_price = int(input('Enter your minimum price: '))
max_price = int(input('Enter your maximum price: '))

new_df = df[(df['Category Name'] == category) & (price >= min_price) & (price <= max_price)]
        

dataframe = sc.get_items(sc.category_dict)

def store():
    pass