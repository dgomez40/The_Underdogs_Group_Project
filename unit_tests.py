"""Your project must include unit tests. 
For each function or method that does not perform input or output, your project 
should include enough test cases to verify that the function or method behaves 
as expected within the full range of expected conditions under which that 
function or method might be called. Provide enough comments, docstrings, and 
self-documenting code features (e.g., descriptive variable names) to make it 
clear what cases you are testing and why.
"""

# Example code from Exercise 4:

"""def test1():
    # Ties
    assert rps1("scissors", "scissors") == 0
    assert rps1("rock", "rock") == 0
    assert rps1("paper", "paper") == 0"""
    
from store import manipulate_df
from store import store
import pandas as pd
import scraper as sc
from scraper import Categories
from scraper import Items

def scraper_test():
    
    # just for testing purposed
    partial_url = '/test-sites/e-commerce/allinone/phones'
    name = 'Phones'
    
    # testing to see if the get_subcategory_urls method in the Categories class in the scraper script returns a list
    assert isinstance (Categories(partial_url, name).get_subcategory_urls(), list)
    
    # testing to see if the get_subcategory_names method in the Categories class in the scraper script returns a list
    assert isinstance (Categories(partial_url, name).get_subcategory_names(), list)
    
    # testing to see if the get_subcategories method in the Categories class in the scraper script returns a dictionary
    assert isinstance (Categories(partial_url, name).get_subcategories(), dict)
    
    url = 'https://webscraper.io/test-sites/e-commerce/allinone'
    
    # testing to see if the get_categories function in the scraper script returns a list
    assert isinstance (sc.get_categories(url), list)
    
    # testing to see if the get_items function in the scraper script returns a data frame
    assert isinstance (sc.get_items(url), pd.DataFrame)

def store_tests():
    
    # testing manupulate_df by seeing if the dataframe returned by the function is not empty
    new_df = manipulate_df()
    assert not new_df.empty
   
    
if __name__ == '__main__':
    
    scraper_test()
    store_tests()