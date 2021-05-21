#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
data_ingestion.py

Helper functions for assembling dataset to be used in algorithms

Author: Matthew Garton
"""
import os
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange

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
        Frequency of data to return. The default is 'Daily'.
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
    Historical stock price data in standardized dataframe format
    """
    
    if source == 'av':
        # instantiate a TimeSeries object to make calls for ts data
        ts = TimeSeries(
            key=os.getenv('ALPHAVANTAGE_API_KEY'), 
            output_format='pandas'
            )
        
        # request data at desired frequency
        # TODO: implement methods for other frequencies
        data, meta = ts.get_daily(symbol, outputsize='full')
        
        # data must be sorted ascending by date
        data.sort_index(ascending=True, inplace=True)
        
        # rename av's format to standard
        # TODO: add documentation explaining standard data format
        data.rename(
            columns={
                '1. open': 'open',
                '2. high': 'high',
                '3. low': 'low',
                '4. close': 'close',
                '5. volume': 'volume'
                },
            inplace=True
            )
    elif source == 'iex':
        raise NotImplementedError('IEX functionality is not set up. Use another source')
        
    return data


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
        source,
        freq='Daily',
        start_date=None,
        end_date=None
        ):
    """
    Wrapper function for retrieving historical forex prices from various APIs

    Parameters
    ----------
    base : str
        currency you are 'buying' or converting 'to'; 'to_currency' in the AV
        framework
    price : str
        currency you are 'selling' or converting 'from'; 'from_currency' in
        the AV framework
    source : str
        source for retrieving the data; defaults to 'av'
    freq : str, default 'Daily'
        frequency of data; defaults to daily
    start_date : datetime, default None
        earliest date to pull prices; if None returns the full dataset
    end_date : datetime, default None
        last date to pull prices; if None then return the full dataset

    Returns
    -------
    Historical forex data in standardized dataframe format

    """
    
    if source == 'av':
        fx = ForeignExchange(
            key=os.getenv('ALPHAVANTAGE_API_KEY'),
            output_format='pandas'
            )
        data, meta = fx.get_currency_exchange_daily(price, base)
        
        # data must be sorted ascending by date
        data.sort_index(ascending=True, inplace=True)
        
        # rename av's format to standard
        # TODO: add documentation explaining standard data format
        data.rename(
            columns={
                '1. open': 'open',
                '2. high': 'high',
                '3. low': 'low',
                '4. close': 'close'
                },
            inplace=True
            )
    return data
    

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