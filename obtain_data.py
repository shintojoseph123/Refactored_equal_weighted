
# coding: utf-8

# In[ ]:

from close_price import close_price

def quarterly_returns(start_year ,end_year,stocks):
    """
    obtainig data from yahoo finance
    
    Parameters
    ----------
    start_year : Starting year of the stock data to be needed.
    end_year : Ending year of the stock data to be needed.
    
    Returns
    -------
    Quarterly returns of symbol in requested period.
    """
    # obtaining the TICKER symbols of the stocks
    stock = stocks
    print (stock)
    
    # initialising start date and end date    
    start_date =  start_year
    end_date = end_year

    
    # creating dictionary to store the quarterly returns
    stock_data = {}
    
    # for each TICKER symbol in stock obtain the quarterly returns    
    for abbv in stock:
        query = str(abbv)+".NS"
        
        # obtaining data        
        stock_data[abbv] = close_price(query,start=start_date, end=end_date )
        
        # filtering to obtain quarterly data 
        stock_data[abbv] = stock_data[abbv].resample('Q').last()
        
        # finding the returns
        stock_data[abbv] = stock_data[abbv].pct_change(1)
   
    return stock_data


def quarterly_price(start_year ,end_year,stocks):
    """
    function to obtain quarterly price data
    
    Parameters
    ----------
    start_year : starting year from which stock data is to be obtained
    end_year : ending year of the stock data to be obtained
    
    Returns
    -------
    returns quarterly_price_data
    """
    
    # obtaining the TICKER symbols of the stocks
    stock = stocks
    
    # initialising start date and end date 
    start_date =  start_year
    end_date = end_year

    
    # creating dictionary to obtain quarterly_price_data
    quarterly_price_data = {}
    
    # for each TICKER symbol in stock
    for abbv in stock:
        # add TICKER symbol with .NS to obtain National Stock exchange TICKER symbol
        query = str(abbv)+".NS"
        
        # obtain all the price_data
        quarterly_price_data[abbv] = close_price(query,start=start_date, end=end_date )
        
        # filter quarterly price_data
        quarterly_price_data[abbv] = quarterly_price_data[abbv].resample('Q', how='last')

   
    return quarterly_price_data

