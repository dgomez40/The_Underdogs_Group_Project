import scraper as  sc
import tabulate as tb



df = sc.get_items("https://webscraper.io/test-sites/e-commerce/allinone")

df['Price'] = df['Price'].str.replace('$', '').astype(float)

category = input('Choose your category between Phones and Computers: ').capitalize()

min_price = float(input('Enter your minimum price: '))
max_price = float(input('Enter your maximum price: '))

new_df = df[(df['Category Name'] == category) & (df['Price'] >= min_price) & (df['Price'] <= max_price)]
new_df = new_df.reset_index(drop=True)


def add_cart(cart, item):
    cart.append(item)
    
cart = []


if len(new_df) != 0:
    
    print('What is in stock based on your price range:')
    for num, item in new_df.iterrows():
        print(f"{num + 1}. {item['Item Name']} ${item['Price']}")
        
    while True:
        
        choice = int(input('Enter the item number of the item you want to see details for: '))
        
        if choice != 0:
        
            item_selection = new_df.iloc[choice - 1]
            
            print(f"Item Name: {item['Item Name']}")
            print(f"Item URL: {item['Item URL']}")
            print(f"Price: ${item['Price']}")
            print(f"Description: {item['Description']}")
            print(f"Stars: {item['Stars']}")
            print(f"Reviews: {item['Reviews']}")
            print(f"Variants: {item['Variants']}")
            print(f"Colors: {item['Colors']}")
            
        ask_to_add = input('Would you like to add this item to the cart? ').lower
        if ask_to_add == 'yes':
            add_cart(cart, item_selection)
            keep_shopping = input('Would you like to keep shopping? ')
                
            if keep_shopping == 'yes':
                break
                
        elif ask_to_add == 'no':
                
            break
        
    else:
        quit

else:
    quit
                                       

empty = True

if cart is not empty:
    total_price = sum(item['Price'] for item in cart)
    print(f'Your total is: ${total_price}')
else:
    quit

        


