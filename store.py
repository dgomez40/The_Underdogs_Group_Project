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
    html = urllib.request.urlopen(url, context=ctx).read().decode('utf-8')
    urls = []
    index = 0
    partial_urls = re.findall("(?<=href=\")/test-sites/e-commerce/allinone(?!/product/)[^\"]*(?=\")", html)
    category_names = re.findall("(?<=class=\"nav-link\">).*|(?<=nav-link \">\n)\s*(.*)(?=\n)")
    for address in partial_urls:
        # print(url)
        urls.append(f"https://webscraper.io{url}")
    for address in urls:
        if address != url:
            sub_html = urllib.request.urlopen(address, context=ctx).read().decode('utf-8')
            sub_urls = re.findall("(?<=href=\")/test-sites/e-commerce/allinone(?!/product/)[^\"]*(?=\")", sub_html)
            sub_names = re.findall("(?<=class=\"nav-link\">).*|(?<=nav-link \">\n)\s*(.*)(?=\n)")
            
        
    # if regex is not None:
    #     category_url = f"https://webscraper.io + {regex.string}"
    #     print(category_url)        
    # if category_url != url:
    #     category_name = html_array.index(index+1)
    # elif category_url url
    # index += 1

    
    
# # def categories_to_csv():    

    

# # def items_to_csv():
    

#get_categories("https://webscraper.io/test-sites/e-commerce/allinone")
get_items("https://webscraper.io/test-sites/e-commerce/allinone")
    
        
    
    
    
    
        
    











