import store as st
import pandas as pd
import scraper as sc

def scraper_test():
    
    # just for testing purposes
    partial_url = '/test-sites/e-commerce/allinone/phones'
    name = 'Phones'
    
    # testing to see if the get_subcategory_urls method in the Categories class in the scraper script returns a list
    assert isinstance (sc.Categories(partial_url, name).get_subcategory_urls(), list)
    
    # testing to see if the get_subcategory_names method in the Categories class in the scraper script returns a list
    assert isinstance (sc.Categories(partial_url, name).get_subcategory_names(), list)
    
    # testing to see if touch (a known subcategory) is in the list of subcategories under the Phones category
    assert "Touch" in sc.Categories(partial_url, name).get_subcategory_names()
    
    # testing to see if the get_subcategories method in the Categories class in the scraper script returns a dictionary
    assert isinstance (sc.Categories(partial_url, name).get_subcategories(), dict)
    
    url = 'https://webscraper.io/test-sites/e-commerce/allinone'
    
    # testing to see if the get_categories function in the scraper script returns a list
    assert isinstance (sc.get_categories(url), list)
    
    # testing to see if the get_items function in the scraper script returns a data frame
    assert isinstance (sc.get_items(url), pd.DataFrame)
    
    # testing to see if the data frame returned by get_items isn't empty
    assert not sc.get_items(url).empty

def store_tests():
    
    dataframe = st.manipulate_df()
    
    # testing to see if the manipulate_df function in the store script returns a data frame
    assert isinstance (dataframe, pd.DataFrame)
    
    # testing manipulate_df by seeing if the dataframe returned by the function is not empty
    assert not dataframe.empty
    
    # cart = []
    
    # st.add_cart(cart, "bruh")
    
    # # testing whether add_cart can add to cart
    # assert "bruh" in cart
   
    
if __name__ == '__main__':
    
    scraper_test()
    store_tests()