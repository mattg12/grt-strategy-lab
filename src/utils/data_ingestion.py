#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
data_ingestion.py

Helper functions for assembling dataset to be used in algorithms

Author: Matthew Garton
"""

def get_stock_prices(
        symbol, 
        source,
        freq='Daily',
        start_time=None, 
        end_time=None, 
        ):
    """
    Wrapper function for retrieving stock price data from various APIs
    
    Parameters
    ----------
    universe : str
        Ticker or list of tickers to return price data for.
    freq : str, optional
        DESCRIPTION. The default is 'Daily'.
    start_time : date, optional
        Earliest timestamp to return. The default is None. Default behaviour
        will return the earliest available data
    end_time : date, optional
        Most recent start time to return. The default is None. Default behaviour
        returns up to the most recent datapoint
    source : str
        Source to pull data from. Supported sources for now are:
        - 'iex' for IEX Cloud
        - 'av' for 'AlphaVantage'

    Returns
    -------
    Historical stock price data in the format specified by the data provider.
    See relevant provider's API documentation for details on output format.
    """
    
    if source=='av':
        pass
    elif source=='iex':
        pass
        
    return None


def get_futures_prices(
        contract,
        start_date,
        end_date,
        source
        ):
    """
    Wrapper function for retrieving historical futures prices from various APIs

    Parameters
    ----------
    universe : TYPE
        DESCRIPTION.
    start_date : TYPE
        DESCRIPTION.
    end_date : TYPE
        DESCRIPTION.
    source : TYPE
        DESCRIPTION.
    roll_method : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    return None


def get_forex_prices(
        base,
        price,
        tenor,
        start_date,
        end_date,
        source
        ):
    """
    Wrapper function for retrieving historical forex prices from various APIs

    Parameters
    ----------
    base : TYPE
        DESCRIPTION.
    price : TYPE
        DESCRIPTION.
    tenor : TYPE
        DESCRIPTION.
    start_date : TYPE
        DESCRIPTION.
    end_date : TYPE
        DESCRIPTION.
     : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    return None
    

def get_option_prices(
        contract,
        start_date,
        end_date,
        freq,
        source
        ):
    """
    Wrapper function for retrieving option prices from various APIs

    Parameters
    ----------
    contract : TYPE
        DESCRIPTION.
    start_date : TYPE
        DESCRIPTION.
    end_date : TYPE
        DESCRIPTION.
    freq : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """


def create_continuous_futures_history(
        contracts,
        start_date,
        end_date,
        roll_method
        ):
    """
    Turn raw futures data into a continuous price history, accounting for the
    roll at expiry

    Parameters
    ----------
    contracts : TYPE
        DESCRIPTION.
    start_date : TYPE
        DESCRIPTION.
    end_date : TYPE
        DESCRIPTION.
    roll_method : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """