
# coding: utf-8

# In[ ]:

# from stock_performance import stock_performance
import numpy as np

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot
        
def plot_performance_graph(start_year,end_year):
    """
    plot the performance graph of stocks
    """
    
    # obtaining normalised returns of the all stocks to all_returns
    all_returns = stock_performance(start_year,end_year,stocks)
    
    # plotting performance graph  using performance_graph() function
    performance_graph(all_returns,stocks)
    

def performance_graph(all_returns,stocks):
    """
    plotting the performance graph of all stocks
    
    Parameters
    ----------
    all_returns :normalised returns of the all stocks
    """
    
    # obtaining the TICKER symbols of the stocks    
    stock = stocks

    # converting into numpy array for calculation
    all_returns = np.array(all_returns)
    shap = all_returns.shape
    row = shap[0]
    column = shap[1]
    
    # calculating the x and y axis of graph
    x_axis = []
    for k in range(column):
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

