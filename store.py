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
    def __init__(self, partial_url, name):
        self.partial_url = partial_url
        self.name = name
        self.category = {name : f"https://webscraper.io{partial_url}"}
    def get_category(self):
        # print(f"get_category returned {self.category}.")
        return self.category
        # subcategories = {}
        # self.subcategories = subcategories
    def get_subcategory_urls(self):
        self.raw_sub_urls = re.findall(
            f"(?<=href=\"){self.partial_url}/(?!product/)[^\"]*(?=\")",
            self.sub_html)
        sub_urls = []
        for sub_address in self.raw_sub_urls:
            sub_urls.append(f"https://webscraper.io{sub_address}")
        # print(f"get_subcategory_urls returned {sub_urls}.")
        return sub_urls
    def get_subcategory_names(self):
        raw_sub_names = re.findall(
            "(?<=nav-link subcategory-link \">\n).*(?=\n)", self.sub_html)
        sub_names = []
        for name in raw_sub_names:
            sub_names.append(name.strip())
        # print(f"get_subcategory_urls returned {sub_names}.")
        return sub_names
    def get_subcategories(self):
        self.sub_html = urllib.request.urlopen(
            f"https://webscraper.io{self.partial_url}",
            context=ctx).read().decode('utf-8')
        sub_names = self.get_subcategory_names()
        sub_urls = self.get_subcategory_urls()
        sub_dict = dict(zip(sub_names, sub_urls))
        return sub_dict

        
    # def :
        

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
            
        
    # if regex is not None:
    #     category_url = f"https://webscraper.io + {regex.string}"
    #     print(category_url)        
    # if category_url != url:
    #     category_name = html_array.index(index+1)
    # elif category_url url
    # index += 1

def get_categories(url):
    html = urllib.request.urlopen(url, context=ctx).read().decode('utf-8')
    names = []
    obj_list = []
    partial_urls = re.findall("(?<=href=\")/test-sites/e-commerce/allinone/(?!product/)[^\"]*(?=\")", html)
    # print(partial_urls)
    # Example partial_url: '/test-sites/e-commerce/allinone/computers'
    raw_names = re.findall("(?<=nav-link \">\n).*(?=\n)", html)
    # Or use (?<=class=\"nav-link\">).*(?=<)|(?<=nav-link \">\n)\s*.*(?=\n) if
    # you want to get the Home category as well -- make sure to add +1 to the
    # names index in the obj_list.append() statement above the return statement.
    # Example raw_names: ['Home', '\t\t\t\t\tComputers', '\t\t\t\t\tPhones']
    # print(raw_names)
    for name in raw_names:
        names.append(name.strip())
        # Example names: ['Home', 'Computers', 'Phones']
    for num in range(0, len(partial_urls)):
        obj_list.append(Categories(partial_urls[num], names[num]))
    return obj_list

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
    
    
category_dict = {}

for object in get_categories("https://webscraper.io/test-sites/e-commerce/allinone"):
    print(object.get_category())
    print(object.get_subcategories())
    
# get_items("https://webscraper.io/test-sites/e-commerce/allinone")

    
        
    











