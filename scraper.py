"""
NOTE: TO ALLOW THIS PROGRAM TO FUNCTION, PLEASE RUN THE FOLLOWING:

pip install regex

pip install tabulate

The former command is for installing a better version of regex with support
for \K, and the latter allows for more readable and aesthetically-pleasing
printouts of Pandas dataframes.

"""


# Import relevant modules:
import urllib.request, urllib.parse, urllib.error
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

import pandas as pd
from tabulate import tabulate
import regex

# Objects:

class Categories():
    def __init__(self, partial_url, name):
        self.partial_url = partial_url
        self.name = name
        self.url = f"https://webscraper.io{partial_url}"
        self.category_html = urllib.request.urlopen(
            f"https://webscraper.io{self.partial_url}",
            context=ctx).read().decode('utf-8')
    def get_subcategory_urls(self):
        self.raw_sub_urls = regex.findall(
            f"(?<=href=\"){self.partial_url}/(?!product/)[^\"]*(?=\")",
            self.category_html)
        sub_urls = []
        for sub_address in self.raw_sub_urls:
            sub_urls.append(f"https://webscraper.io{sub_address}")
        # print(f"get_subcategory_urls returned {sub_urls}.")
        return sub_urls
    def get_subcategory_names(self):
        raw_sub_names = regex.findall(
            "(?<=nav-link subcategory-link \">\n).*(?=\n)", self.category_html)
        sub_names = []
        for name in raw_sub_names:
            sub_names.append(name.strip())
        # print(f"get_subcategory_urls returned {sub_names}.")
        return sub_names
    def get_subcategories(self):
        sub_names = self.get_subcategory_names()
        sub_urls = self.get_subcategory_urls()
        sub_dict = dict(zip(sub_names, sub_urls))
        return sub_dict

"""
Conceptual design for the Pandas dataframe:

Category Name

Subcategory Names

Subcategory URLs

Item Names

Item URLs

Item Prices

Item Descriptions

Item Variants (Computers)

Item Colors (Phones)

"""


class Items():
    def __init__(self, cat_obj):
        self.cat_obj = cat_obj
        self.cat_name = cat_obj.name
        self.cat_url = cat_obj.url
        self.sub_cat_names = cat_obj.get_subcategory_names()
        self.get_category_items()
        self.get_subcategory_items()
        self.raw_items = self.make_df()
        self.raw_items.insert(0, 'Category Name', self.cat_name)
    def get_items(self, url):
        html = urllib.request.urlopen(url,
                                    context=ctx).read().decode('utf-8')
        item_names = regex.findall(
            '(?<=title=\").*(?=\")', html
            )

        raw_item_urls = regex.findall(
            '(?<=<a href=\")/test-sites/e\-commerce/allinone/product/\d*', html
        )
        
        item_urls = []
        for partial_url in raw_item_urls:
            item_urls.append(f"https://webscraper.io{partial_url}"
            )

        item_prices = regex.findall(
            'price float-end card-title pull-right\".(.*)<', html
            )

        item_descriptions = regex.findall(
            'description card-text\".(.*)<', html
            )

        item_stars = regex.findall(
            'data-rating=\"(.*)\"', html
            )

        item_review_counts = regex.findall(
            'review-count float-end\">(.*)<', html
            )

        return(item_names,
               item_urls,
               item_prices,
               item_descriptions,
               item_stars,
               item_review_counts)
        
        
    
    def get_category_items(self):
        items = self.get_items(self.cat_url)
        self.item_names = items[0]
        # print(self.item_names)
        self.item_urls = items[1]
        self.item_prices = items[2]
        self.item_descriptions = items[3]
        self.item_stars = items[4]
        self.item_review_counts = items[5]

    def get_subcategory_items(self):
        for address in self.cat_obj.get_subcategory_urls():
            items = self.get_items(address)
            self.item_names.extend(items[0])
            # print(self.item_names)
            self.item_urls.extend(items[1])
            self.item_prices.extend(items[2])
            self.item_descriptions.extend(items[3])
            self.item_stars.extend(items[4])
            self.item_review_counts.extend(items[5])
    
    def make_df(self):
        items_df = pd.DataFrame(list(zip(self.item_names,
                            self.item_urls,
                            self.item_prices,
                            self.item_descriptions,
                            self.item_stars,
                            self.item_review_counts
                            )),
                    columns=['Item Name',
                            'Item URL',
                            'Price',
                            'Description',
                            'Stars',
                            'Reviews'])
        return items_df

class Computers(Items):
    def __init__(self, cat_obj):
        super().__init__(cat_obj)
        # items_obj = Items(cat_obj)
        items = self.raw_items
        # print(items_df)
        variants = self.get_item_variants()
        self.variants = pd.Series(variants)
        items["Variants"] = self.variants
        self.items = items

    def get_item_variants(self):
        variants = []
        for item_address in self.item_urls:
            item_html = urllib.request.urlopen(item_address,
                                               context=ctx).read(
                                                   ).decode('utf-8')
            variants.append(
                regex.findall('active\W+value=\"\K\d+|swatch\W+value=\"\K\d+',
                              item_html))
        return variants

class Phones(Items):   
    def __init__(self, cat_obj):
        super().__init__(cat_obj)
        items = self.raw_items
        colors = self.get_item_colors()
        self.colors = pd.Series(colors)
        items["Colors"] = self.colors
        self.items = items

    def get_item_colors(self):
        colors = []
        for item_address in self.item_urls:
            item_html = urllib.request.urlopen(item_address,
                                               context=ctx).read(
                                                   ).decode('utf-8')
            colors.append(
                regex.findall('value=\"(.*)\"(?!>Select)', item_html))
        return colors

def get_categories(url):
    html = urllib.request.urlopen(url, context=ctx).read().decode('utf-8')
    names = []
    obj_list = []
    partial_urls = regex.findall(
        "(?<=href=\")/test-sites/e-commerce/allinone/(?!product/)[^\"]*(?=\")",
        html)
    raw_names = regex.findall("(?<=Navigation category\">\n).*(?=\n)", html)
    print("Number of names" + str(len(raw_names)))
    for name in raw_names:
        names.append(name.strip())
        # Example names: ['Home', 'Computers', 'Phones']
    for num in range(0, len(partial_urls)):
        obj_list.append(Categories(partial_urls[num], names[num]))
    return obj_list

def get_items(url):
    obj_list = get_categories(url)
    for obj in obj_list:
        if obj.name == "Computers":
            computers_obj = Computers(obj)
            computers = computers_obj.items
            # print(tabulate(computers.items,
            # headers = 'keys', tablefmt = 'pretty'))
        if obj.name == "Phones":
            phones_obj = Phones(obj)
            phones = phones_obj.items
            # print(tabulate(phones.items,
            # headers = 'keys', tablefmt = 'pretty'))
    items = pd.concat([computers, phones], axis=0, ignore_index=True)
    return items.drop_duplicates(subset="Item URL").reset_index(drop=True)

if __name__ == "__main__":
    df = get_items("https://webscraper.io/test-sites/e-commerce/allinone")
    
    print(tabulate(df, headers = 'keys', tablefmt = 'pretty'))
    
    df.to_csv("output.csv")