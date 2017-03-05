
# coding: utf-8

# In[ ]:

import numpy as np

def total_profit(input_price,beg ,stock_data,quarterly_price_data,stocks):
    """
    finds the total profit and number of quarters and returns a list
    
    Parameters
    ----------
   
    input_price : amount to buy the stocks
    beg : variable to loop through 
    stock_data : Quarterly price data
    quarterly_price_data :quarterly price data
    
    """
    
    # obtaining the TICKER symbols of the stocks     
    stock = stocks
    
    # obtaining Quarterly returns of stock data  
    stock_data = stock_data
    
    # finding the number of stocks    
    no_of_stocks = len(stock)
    
    # calculating each stock price   
    each_stock_price = int(input_price)/no_of_stocks
    
    
    # list to store all return values 
    all_profits = []
    
    # for each TICKER symbol in stock
    for abbv in stock:
        # obtaining quarterly price data        
        stock_data[abbv] = quarterly_price_data[abbv]
        
        # converting to numpy array for calculation        
        data = np.array(stock_data[abbv])
        
        # calculating number of stocks can be buyied
        number_of_stocks = each_stock_price/int(data[beg])

        # obtainig price data    
        quart_ret = stock_data[abbv]
        
        # filtering to obtain quarterly price data        
        quart_ret = quart_ret.resample('Q', how='last')
        
        # finding the profit or loss
        quart_ret = quart_ret.diff()

        # converting into numpy array
        data = np.array(quart_ret)
        
        #creating a list to convert numpy into a list of float of values
        val = []
        for i in data:
            if np.isnan(i):
                i = float(0)
                val.append(i)
            else:
                i = float(i)
                val.append(i)
        
        # slicing to remove the first data from list ,ie:0  
        quart_ret = val[1:]

        # taking the beg position value  
        rets = quart_ret[beg]
        
        # find the total profit of stock
        tot_ret = number_of_stocks*rets


        # add all the profits to the all returns list
        all_profits.append(tot_ret)
    
    # create a list to store the profit and number of quarters
    portfolio_ret = []
    
    # sum all the profits of all stocks
    col_sum = sum(all_profits)
    
    # append all profit to portfolio_ret[] list
    portfolio_ret.append(col_sum)
    
    # append number of quarters to portfolio_ret[] list
    portfolio_ret.append(len(quart_ret))
    
    
    return portfolio_ret

