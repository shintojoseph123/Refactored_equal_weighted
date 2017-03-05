
# coding: utf-8

# In[ ]:

from obtain_data import quarterly_returns
import numpy as np
import pyfolio as pf


def stock_performance(start_year,end_year,stocks):
    """
    function to check performance of stock
    
    Parameters
    ----------
    start_year : starting year to obtain stock data
    end_year : ending year to obtain stock data
    
    Returns
    -------
    returns a list of normalised returns of all stocks
    """
    
    # obtaining the TICKER symbols of the stocks
    stock = stocks
    
    # create a list to obtain all the returns of the stock
    all_returns = []

    # obtaining Quarterly returns using quarterly_returns() function
    stock_data = quarterly_returns(start_year,end_year,stocks)
    

    # for each TICKER symbol in stock    
    for abbv in stock:
        data = stock_data[abbv]

        
        # creating pyfolio tearsheet
#         pf.create_returns_tear_sheet(data)

        # changing into numpy array for calculation
        data = np.array(data)
        
        # creating a list to remove the NaN and make it a list of float values 
        val = []
        for i in data:
            if np.isnan(i):
                i = float(0)
                val.append(i)
            else:
                i = float(i)
                val.append(i)
                
        # normalising to 100
        norm = 100
        for i in range(len(val)):
            push = (1+val[i])*norm
            val[i] = push
            norm = push

        # adding the normalised returns of all stocks to the all_returns[] list
        all_returns.append(val)

    return all_returns


