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
import pandas

# Objects:

class Categories():
    def __init__(self, partial_url, name):
        self.partial_url = partial_url
        self.name = name
        self.url = f"https://webscraper.io{partial_url}"
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

class Items():
    def __init__(self, cat_obj):
        self.cat_obj = cat_obj
        self.cat_name = cat_obj.name
        self.cat_url = cat_obj.url
        self.cat_names = []
        self.sub_cat_names = []
        self.item_names = []
        
    def get_parent_items(self):
        item_names = self.get_item_names(self.cat_url)
        
        parent_dict = dict()
        
    def get_child_items(self):
        
    def get_item_names(self, url):
        
    def category(self, url):
        pass
    def price(self, url):
        pass
    def reviews(self, url):
        pass
    def stars(self, url):
        """html = urllib.request.urlopen(
                obj.url, context=ctx).read().decode('utf-8')
            item_name = re.findall(
                '(?<=title=\").*(?=\")', html
                )
            item_price = re.findall(
                'price float-end card-title pull-right\".(.*)<', html
                )
            item_description = re.findall(
                'description card-text\".(.*)<', html
                )
            item_stars = re.findall(
                'data-rating=\"(.*)\"', html
                )
            item_review_count = re.findall(
                'review-count float-end\">(.*)<', html
                )"""


# class Computers(Items):
    
#     def __init__():
        
#     def description():

#     


# class Phones(Items):   

#     def __init__():
    
#     def features():

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

def get_items(obj_list):
    for obj in obj_list:
        print(obj.name)
        if obj.name == "Computers":
            items = Computers(obj)
            pass
        elif obj.name == "Phones":
            items = Phones(obj)
            pass
        else:
            items = Items(obj)
        
    #item_color = re.findall('class=\"dropdown-item\" value=\"(.*)\"', html)
    #print(str(item_color))

# # def items_to_csv():
    
category_dict = {}

obj_list = get_categories(
    "https://webscraper.io/test-sites/e-commerce/allinone"
    )

get_items(obj_list)
    
# get_items("https://webscraper.io/test-sites/e-commerce/allinone")

def store():
    pass

    
        
    











