# Copyright 2021 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# TODO: Import any required packages here


import utilities

def get_token():
    '''Returns personal access token. Only required if submitting to autograder.'''
    
    # TODO: Fill in your API token below if using the autograder
    return 'YOUR-TOKEN-HERE'

def define_variables(stockcodes):
    """Define the variables to be used for the CQM.
    Args:
        stockcodes (list): List of stocks under consideration
    
    Returns:
        stocks (list): 
            List of variables named 's_{stk}' for each stock stk in stockcodes, where stk is replaced by the stock code.
    """

    # TODO: Define your list of variables and call it stocks
    ## Hint: Remember to import the required package at the top of the file for Binary variables
    


    return stocks

def define_cqm(stocks, num_stocks_to_buy, price, returns, budget, variance):
    """Define a CQM for the exercise. 
    Requirements:
        Objectives: 
            - Maximize returns
            - Minimize variance
        Constraints:
            - Choose exactly num_stocks_to_buy stocks
            - Spend at most budget on purchase
            
    Args:
        stocks (list):
            List of variables named 's_{stk}' for each stock in stockcodes
        num_stocks_to_buy (int): Number of stocks to purchase
        price (list):
            List of current price for each stock in stocks
                where price[i] is the price for stocks[i]
        returns (list):
            List of average monthly returns for each stock in stocks
                where returns[i] is the average returns for stocks[i]
        budget (float):
            Budget for purchase
        variance (2D numpy array):
            Entry [i][j] is the variance between stocks i and j
        
    Returns:
        cqm (ConstrainedQuadraticModel)
    """

    # TODO: Initialize the ConstrainedQuadraticModel called cqm
    ## Hint: Remember to import the required package at the top of the file for ConstrainedQuadraticModels
    

    # TODO: Add a constraint to choose exactly num_stocks_to_buy stocks
        

    # TODO: Add a constraint that the cost of the purchased stocks is less than or equal to the budget


    # TODO: Add an objective function maximize returns AND minimize variance
    ## Hint: Determine each objective separately then add them together
    ## Hint: Variance is computed as a quadratic term: variance[i][j]*stock[i]*stock[j]


    return cqm

def sample_cqm(cqm):

    # TODO: Define your sampler as LeapHybridCQMSampler
    ## Hint: Remember to import the required package at the top of the file
    

    # TODO: Sample the ConstrainedQuadraticModel cqm and store the result in sampleset


    return sampleset

if __name__ == '__main__':

    # 10 stocks used in this program
    stockcodes = ["T", "SFL", "PFE", "XOM", "MO", "VZ", "IBM", "TSLA", "GILD", "GE"]

    price, returns, variance = utilities.get_stock_info()

    # Number of stocks to select
    num_stocks_to_buy = 2

    # Set the budget
    budget = 40

    # Add binary variables for stocks
    stocks = define_variables(stockcodes)

    # Build CQM
    cqm = define_cqm(stocks, num_stocks_to_buy, price, returns, budget, variance)

    # Run CQM on hybrid solver
    sampleset = sample_cqm(cqm)
    
    # Process and print solution
    print("\nPart 3 solution:\n")
    utilities.process_sampleset(sampleset, stockcodes)
