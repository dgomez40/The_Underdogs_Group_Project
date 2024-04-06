# Import relevant modules:

import re
# Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
# import re
import ssl
import html
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Objects:

# class Categories():
    
#     def __init__():
        
#     def category_name():
        
#     def subcategories():
        
#     def url():
        

# class Computers():
    
#     def __init__():
        
#     def item_name():
        
#     def description():
        
#     def category():
        
#     def price():
        
#     def reviews():
    
#     def stars():



# class Phones():
    
#     def __init__():
    
#     def item_name():
    
#     def features():
    
#     def category():
        
#     def price():
        
#     def reviews():
        
#     def stars():     

# Non-class functions:
    
def get_categories(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    html_array = str(html).split("\\n")
    del html_array[:133]
    del html_array[176:]
    categories_array = []
    index = 0
    for line in html_array:
        regex = re.search("(?<=href=\")[^\"]*(?=\")", line)
        if regex is not None:
            category_url = "https://webscraper.io" + regex.string
            print(category_url)        
        # if category_url != url:
        #     category_name = html_array.index(index+1)
        # elif category_url url
        # index += 1

    
    
# # def categories_to_csv():    

# def get_items():

# # def items_to_csv():
    

get_categories("https://webscraper.io/test-sites/e-commerce/allinone")
    
        
    
    
    
    
        
    











