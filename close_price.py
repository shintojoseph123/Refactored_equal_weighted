
# coding: utf-8

# In[ ]:

from pandas_datareader import data as web
import pandas as pd



def close_price(symbol, start=None, end=None):
    """
    Gets returns for a symbol.
    Queries Yahoo Finance
    
    Parameters
    ----------
    symbol : Ticker symbol, e.g. APPL.
    start : start date.
    end : end date.
    
    Returns
    -------
    Close price for the symbol.

    """

    if start is None:
        start = '1/1/1970'
    if end is None:
        end = _1_bday_ago()

    start = get_utc_timestamp(start)
    end = get_utc_timestamp(end)
    
    # get returns from yahoo
    close = get_symbol_from_yahoo(symbol, start=start, end=end)


    return close[symbol]


def get_utc_timestamp(dt):
    """
    Returns the Timestamp/DatetimeIndex
    with either localized or converted to UTC.
    
    Parameters
    ----------
    dt : Timestamp/DatetimeIndex
        the date(s) to be converted
        
    Returns
    -------
    date(s) converted to UTC
    """

    dt = pd.to_datetime(dt)
    try:
        dt = dt.tz_localize('UTC')
    except TypeError:
        dt = dt.tz_convert('UTC')
    return dt



def get_symbol_from_yahoo(symbol, start=None, end=None):
    """
    Retrieves close prices for symbol from yahoo.
    
    Parameters
    ----------
    symbol : Symbol name to load, e.g. 'SPY'
    start : Start date.
    end : End date.
    
    Returns
    -------
    close price of symbol in requested period.
    """
    
    px = web.get_data_yahoo(symbol, start=start, end=end)
    close = px[['Close']].dropna()
    close.index = rets.index.tz_localize("UTC")
    close.columns = [symbol]
    
    return close

