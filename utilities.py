import csv
import numpy as np
import pandas as pd

# Prepare Stock data from the given csv files
def get_stock_info(verbose=False):
    """Read in stock returns and price information from CSV."""

    # Read the lastday's closing price from csv file, 
    # and store them in the list, then convert it as numpy array
    price_read = []
    with open('data/lastday_closing_price.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            price_read.append(row)
    price = np.array(price_read[0],dtype=float)

    # Compute the average monthly returns for each stock
    df_monthreturn = pd.read_csv("data/monthly_returns.csv", index_col='Date')
    ave_monthly_returns = df_monthreturn.mean(axis=0)
    returns = list(ave_monthly_returns)

    # Compute the variance from the monthly returns
    variance = df_monthreturn.cov().values.tolist()

    if verbose:
        print("Data Check")
        print("Monthly return(the first 5 lines):")
        print(df_monthreturn.head(5))
        print("Average monthly return:")
        print(returns)

    return price, returns, variance

# Function to process samples and print the best feasible solution found
def process_sampleset(sampleset, stockcodes):
    """Read in sampleset returned from sample_cqm command and display solution."""

    # Find the first feasible solution
    first_run = True
    feasible = False
    for sample, feas in sampleset.data(fields=['sample','is_feasible']):
        if first_run:
            best_sample = sample
        if feas:
            best_sample = sample
            feasible = True
            break

    # Print the solution as which stocks to buy
    print("Solution:\n")
    if not feasible:
        print("No feasible solution found.\n")
    else:
        print("Best feasible solution found:")
        for stk in stockcodes:
            if best_sample[f's_{stk}'] == 1:
                print(stk)
    print("\n")
