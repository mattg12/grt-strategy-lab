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
from alpha_vantage.cryptocurrencies import CryptoCurrencies

def get_stock_prices(
        symbol, 
        source,
        freq='Daily',
        start_time=None, 
        end_time=None, 
        ):
    """
    Wrapper function for retrieving stock price data from various APIs. Only
    split/dividend adjusted data is supported.
    
    Parameters
    ----------
    universe : str
        Ticker or list of tickers to return price data for.
    freq : str, optional
        Frequency of data to return. The default is 'Daily'.
    start_time : date, optional
        Earliest timestamp to return. The default is None. Default behaviour
        will return the full dataset for Daily, or the most recent 1-2 mo
        for intraday
    end_time : date, optional
        Last timestamp to return. The default is None. Default behaviour
        returns the full dataset for Daily, or most recent 1-2 mo for intraday
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
        if freq == 'Daily':
            data, meta = ts.get_daily_adjusted(symbol, outputsize='full')
        elif (start_time == None) & (end_time == None):
            data, meta = ts.get_intraday(
                symbol,
                interval=freq,
                outputsize='full'
                )
        else:
            raise NotImplementedError('Extended Intraday not supported yet')
            
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
        
        if freq == 'Daily':
            data, meta = fx.get_currency_exchange_daily(
                price,
                base,
                outputsize='Full')
        else:
            data, meta = fx.get_currency_exchange_intraday(
                price,
                base,
                interval=freq,
                outputsize='full'
                )
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
    

def get_crypto_prices(
        symbol,
        market,
        source,
        freq='Daily',
        start_date=None,
        end_date=None
        ):
    """
    Wrapper function for retrieving historical cryptocurrency prices from 
    various APIs

    Parameters
    ----------
    symbol : str
        cryptocurrency for which you want prices
    market : str
        market for which you want crypto prices (ie the 'base' currency)
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
        cc = CryptoCurrencies(
            key=os.getenv('ALPHAVANTAGE_API_KEY'),
            output_format='pandas'
            )
        
        if freq == 'Daily':
            data, meta = cc.get_digital_currency_daily(symbol, market)
        else:
            raise NotImplementedError('Intraday crypto not supported from AV')
        # data must be sorted ascending by date
        data.sort_index(ascending=True, inplace=True)
        
        # rename av's format to standard
        # TODO: add documentation explaining standard data format
        # TODO: figure out and implement column renaming for cryptos
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