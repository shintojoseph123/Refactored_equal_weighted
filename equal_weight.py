
# coding: utf-8

# In[ ]:

# importing libraries

from stock_performance import stock_performance
from obtain_data import quarterly_returns,quarterly_price
from total_profit import total_profit


import numpy as np
import pyfolio as pf
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot



    
def equal_weight(start_year ,end_year,input_price,stocks):
    """
    function to find the returns of equal weighted portfolio and plot it
    
    Parameters
    ----------
    start_year : starting year from which stock data is to be obtained
    end_year : ending year of the stock data to be obtained
    input_price : amount to buy the stocks
    
    """

    # obtaining list of normalised returns of all stocks
    all_returns = stock_performance(start_year,end_year,stocks)
    
    # create a portfolio list to append all the inputs with profits with first input price as its first
    portfolio = [input_price]
    
    # initializing variables    
    loop = 0
    beg = 0
  
    
    # obtaining Quarterly returns using quarterly_returns() function
    stock_data = quarterly_returns(start_year ,end_year,stocks)
    
    # obtainig quarterly_price data 
    quarterly_price_data = quarterly_price(start_year ,end_year,stocks)
    
    # finding total profit 
    if loop == 0:
        
        # obtain total profit 
        portfolio_ret = total_profit(input_price ,beg,stock_data,quarterly_price_data,stocks)
        
        # add total profit with input price
        input_price = input_price + portfolio_ret[0]
        
        # append new input price to the portfolio list
        portfolio.append(input_price)
        
        # obtain number of quarters to the loop variable
        loop = portfolio_ret[1]

    # finding how many quarters and subtracting one as a loop executed above already
    loop = int((loop)-1)
    
    # until the end of quarter
    for i in range(loop):

        beg = beg + 1
        
        # obtain total profit 
        portfolio_ret = total_profit(input_price ,beg,stock_data,quarterly_price_data,stocks)
        
        # add total profit with input price
        input_price = input_price + portfolio_ret[0]
        
        # append new input price to the portfolio list
        portfolio.append(input_price)
 

    
    # obtaining the TICKER symbols of the stocks
    stock = stocks
    
    # obtain quarterly data inorder to draw pyfolio cause pyfolio will draw only in a particular UTC format
    data = stock_data[stock[0]].resample('Q', how='last')
    
    # assign the portfolio values to the above dataset
    for i in range(len(data)):
        data[i]=portfolio[i]

    # finding returns of portfolio
    data = data.pct_change(1)
    
    # plotting tearsheet of portfolio using pyfolio
    pf.create_returns_tear_sheet(data)
       
        
    # changing to numpy array
    data = np.array(data)
    
    # create a list to store normalised portfolio returns 
    norm_portfolio_returns = []  
    for i in data:
        if np.isnan(i):
            i = float(0)
            norm_portfolio_returns.append(i)
        else:
            i = float(i)
            norm_portfolio_returns.append(i)
            


    # normalising to 100
    norm = 100
    for i in range(len(norm_portfolio_returns)):
        push = (1+norm_portfolio_returns[i])*norm
        norm = push
        norm_portfolio_returns[i] = push

    
    # obtaining the TICKER symbols of the stocks
    stock = stocks
    
    # add the TICKER symbol Equal_weighted to the stock inorder to display in graph
    stock.append("Equal_weighted")
    
    # append all the norm_portfolio_returns to all_returns
    all_returns.append(norm_portfolio_returns)
    
    # convert to numpy array
    all_returns = np.array(all_returns)
    shap = all_returns.shape
    row = shap[0]
    column = len(all_returns[0])

    # calculating x and y axis
    x_axis = []
    for k in range(column):
        k = "Q"+str(k)
        x_axis.append(k)

    loop = {}
    for i in range(0,row):
        loop[i] = all_returns[i]

    data = []
    for i in range(0,row):
        trace = go.Scatter(
            x=x_axis,
            y=loop[i],
            fill=None,
            name = stock[i]
        )
        data.append(trace)

    # plotting graph
    plot(data, filename='stock_performance.html')
    

