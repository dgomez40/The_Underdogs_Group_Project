
import scraper as  sc

from colorama import Fore
from colorama import Style

def manipulate_df():
    
    df = sc.get_items("https://webscraper.io/test-sites/e-commerce/allinone")

    df['Price'] = df['Price'].str.replace('$', '').astype(float)
        
    category = input(
        'Choose your category between Phones and Computers: ').capitalize()
        
    if category != 'Phones' and category != 'Computers':
         print(Fore.RED + "Invalid category. Run the code again and "
               "enter a valid category such as Phones or Computers." 
               + Style.RESET_ALL)
         quit()

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
        
        print(Fore.LIGHTBLUE_EX + 'Items in stock based on your price range:' 
              )
        for num, item in df.iterrows():
            print(Fore.YELLOW + f"{num + 1}. {item['Item Name']}"
                  f" ${item['Price']}" + Style.RESET_ALL)

        while True:
            
            choice = int(input('Enter the item number of the item'
                      ' you want to see details for: '))
            
            if choice > 0 and choice <= len(df):
                
                item_selection = df.iloc[choice - 1]
                
                print(Fore.LIGHTGREEN_EX +
                      f"Item Name: {item_selection['Item Name']}"
                      )
                print(Fore.LIGHTGREEN_EX +
                      f"Item URL: {item_selection['Item URL']}"
                      )
                print(Fore.LIGHTGREEN_EX +
                      f"Price: ${item_selection['Price']}" 
                      )
                print(Fore.LIGHTGREEN_EX +
                      f"Description: {item_selection['Description']}" 
                      )
                print(Fore.LIGHTGREEN_EX +
                      f"Stars: {item_selection['Stars']}" 
                      )
                print(Fore.LIGHTGREEN_EX +
                      f"Reviews: {item_selection['Reviews']}" 
                      )
                print(Fore.LIGHTGREEN_EX +
                      f"Variants: {item_selection['Variants']}" 
                      )
                print(Fore.LIGHTGREEN_EX +
                      f"Colors: {item_selection['Colors']}" 
                      + Style.RESET_ALL)
            
                ask_to_add = input('Would you like to add this'
                                    ' item to the cart? yes or no. ').lower()
                
                if ask_to_add == 'yes':
                    add_cart(cart, item_selection)
                    keep_shopping = input('Would you like to keep shopping?'
                                          ' yes or no. ')
                    if keep_shopping.lower() == 'no':
                        break
                    
                elif ask_to_add == 'no':
                    keep_shopping = input('Would you like to keep shopping?'
                                          ' yes or no. ')
                    if keep_shopping.lower() == 'no':
                        break

            else:   
                print(Fore.LIGHTRED_EX + "That is an invalid item number,"
                      " please enter one that is within the range." 
                      + Style.RESET_ALL)   

    else:
        print(Fore.MAGENTA + "There is nothing in stock that fits "
              "within your price range." + Style.RESET_ALL)
        quit

    empty = True
    if cart is not empty:
        total_price = sum(item['Price'] for item in cart)
        print(Fore.LIGHTCYAN_EX + f'Your total is: ${total_price}' 
              + Style.RESET_ALL)
    else:
        print("You did not select anything.")
        
if __name__ == '__main__':
    
    store()


            


