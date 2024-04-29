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

class Categories():
    
    def __init__(self, url, name, subcategories):
        self.url = url
        self.name = name
        # subcategories = {}
        self.subcategories = subcategories
        
    # def category_name():
        
    # def subcategories():
        
    # def url():
        

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
    names = []
    obj_list = []
    index = 0
    partial_urls = re.findall("(?<=href=\")/test-sites/e-commerce/allinone/(?!product/)[^\"]*(?=\")", html)
    # print(partial_urls)
    # Example partial_url: '/test-sites/e-commerce/allinone/computers'
    raw_names = re.findall("(?<=nav-link \">\n)\s*.*(?=\n)", html)
    # Or use (?<=class=\"nav-link\">).*(?=<)|(?<=nav-link \">\n)\s*.*(?=\n) if
    # you want to get the Home category as well -- make sure to add +1 to the
    # names index in the obj_list.append() statement above the return statement.
    # Example raw_names: ['Home', '\t\t\t\t\tComputers', '\t\t\t\t\tPhones']
    # print(raw_names)
    for address in partial_urls:
        urls.append(f"https://webscraper.io{address}")
        # Example url: 'https://webscraper.io/test-sites/e-commerce/allinone'
    for name in raw_names:
        names.append(name.strip())
        # Example names: ['Home', 'Computers', 'Phones']
    for address in partial_urls:
        sub_html = urllib.request.urlopen(f"https://webscraper.io{address}", context=ctx).read().decode('utf-8')
        raw_sub_urls = re.findall(f"(?<=href=\"){address}/(?!product/)[^\"]*(?=\")", sub_html)
        raw_sub_names = re.findall("(?<=nav-link subcategory-link \">\n)\s*.*(?=\n)", sub_html)
        sub_urls = []
        sub_names = []
        for sub_address in raw_sub_urls:
            sub_urls.append(f"https://webscraper.io{sub_address}")
        for name in raw_sub_names:
            sub_names.append(name.strip())
        sub_dict = dict(zip(sub_names, sub_urls))
        # print("Sub dictionary: " + str(sub_dict))
        obj_list.append(Categories(urls[index], names[index], sub_dict))
        index += 1
    return obj_list
            
        
    # if regex is not None:
    #     category_url = f"https://webscraper.io + {regex.string}"
    #     print(category_url)        
    # if category_url != url:
    #     category_name = html_array.index(index+1)
    # elif category_url url
    # index += 1

    
    
# # def categories_to_csv():    

def get_items(url):
    html_code_home_page = urllib.request.urlopen(url, context=ctx).read().decode('utf-8')
    item_name = re.findall('(?<=title=\").*(?=\")', html_code_home_page)
    item_price = re.findall('price float-end card-title pull-right\".(.*)<', html_code_home_page)
    item_description = re.findall('description card-text\".(.*)<', html_code_home_page)
    item_stars = re.findall('data-rating=\"(.*)\"', html_code_home_page)
    item_review_count = re.findall('review-count float-end\">(.*)<', html_code_home_page)
    #item_color = re.findall('class=\"dropdown-item\" value=\"(.*)\"', html_code_home_page)

    print(str(item_name))
    print(str(item_price))
    print(str(item_description))
    print(str(item_stars))
    print(str(item_review_count))
    #print(str(item_color))
    

# # def items_to_csv():
    

for object in get_categories("https://webscraper.io/test-sites/e-commerce/allinone"):
    print(object.url)
    print(object.name)
    print(object.subcategories)
# get_items("https://webscraper.io/test-sites/e-commerce/allinone")

    
        
    











