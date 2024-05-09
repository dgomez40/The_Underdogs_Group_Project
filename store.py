import scraper as  sc
import pandas as pd
import tabulate as tb


df = pd.read_csv('output.csv')

df['Price'] = df['Price'].str.replace('$', '').astype(float)

category = input('Choose your category between Phones and Computers: ').capitalize()

min_price = float(input('Enter your minimum price: '))
max_price = float(input('Enter your maximum price: '))

new_df = df[(df['Category Name'] == category) & (df['Price'] >= min_price) & (df['Price'] <= max_price)]
new_df = new_df.reset_index(drop=True)


def add_to_cart(cart, product):
    cart.append(product)
    
cart = []



if len(new_df) != 0:
    
    print('What is in stock based on your price range:')
    for num, item in new_df.iterrows():
        print(f"{num + 1}. {item['Item Name']} ${item['Price']}")
        
else:
    quit
    

        

# dataframe = sc.get_items(sc.category_dict)

# def store():
#     pass