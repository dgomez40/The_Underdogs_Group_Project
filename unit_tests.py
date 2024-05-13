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

def unit_tests():
    
    # testing manupulate_df by seeing if the dataframe returned by the function is not empty
    filtered_df = manipulate_df()
    assert not filtered_df.empty
   
    
    # # testing store
    assert store() is not None
    
if __name__ == '__main__':
    
    unit_tests()