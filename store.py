import scraper as  sc
import tabulate as tb

def manipulate_df():
    
    df = sc.get_items("https://webscraper.io/test-sites/e-commerce/allinone")

    df['Price'] = df['Price'].str.replace('$', '').astype(float)

    category = input('Choose your category between Phones and Computers: '
                     ).capitalize()

    min_price = float(input('Enter your minimum price: '))
    max_price = float(input('Enter your maximum price: '))

    new_df = df[(df['Category Name'] == category) &
                (df['Price'] >= min_price) & (df['Price'] <= max_price)]
    return new_df.reset_index(drop=True)
    

def add_cart(cart, item):
    cart.append(item)

def store():
    
    df = manipulate_df()
    
    cart = []

    if len(df) != 0:
        
        print('Items in stock based on your price range:')
        for num, item in df.iterrows():
            print(f"{num + 1}. {item['Item Name']} ${item['Price']}")

        while True:
            
            choice = int(input('Enter the item number of the item'
                      ' you want to see details for: '))
            
            if choice > 0 and choice <= len(df):
                
                item_selection = df.iloc[choice - 1]
                
                print(f"Item Name: {item_selection['Item Name']}")
                print(f"Item URL: {item_selection['Item URL']}")
                print(f"Price: ${item_selection['Price']}")
                print(f"Description: {item_selection['Description']}")
                print(f"Stars: {item_selection['Stars']}")
                print(f"Reviews: {item_selection['Reviews']}")
                print(f"Variants: {item_selection['Variants']}")
                print(f"Colors: {item_selection['Colors']}")
                
                ask_to_add = input('Would you like to add this'
                                   ' item to the cart? Yes or no.').lower()
                
                if ask_to_add.lower() == 'yes':
                    
                    add_cart(cart, item_selection)
                    keep_shopping = input('Would you like to keep shopping?'
                                          'Yes or no.')
                    
                    if keep_shopping.lower() == 'no':
                        break
                    
            else:   
                print("That is an invalid item number,"
                      "please enter one that is within the range.")
                

    else:
        print("There is nothing in stock that fits within your price range.")
        quit


    empty = True


    if cart is not empty:
        total_price = sum(item['Price'] for item in cart)
        print(f'Your total is: ${total_price}')
    else:
        print("You did not select anything.")
        
if __name__ == '__main__':
    
    store()


            


