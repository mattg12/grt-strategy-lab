#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mean_reversion.py

Module of helper functions for mean reversion algorithms
Note that it will be more useful in most cases to implement open source
implementations of such tests

@author: Matthew Garton
"""
import numpy as np
from sklearn.linear_model import LinearRegression

def generate_hurst_exponent(ts):
    """
    Generate the Hurst exponent of a time-series. Formulated based on
    the method described in QuantStart article titled 'Basics of Statistical
    Mean Reversion Testing' found here
    https://www.quantstart.com/articles/Basics-of-Statistical-Mean-Reversion-Testing/

    Rule of thumb:
        if H < 0.5: the series exhibits stationarity; mean reversion strategies
            may work
        if H = 0.5: the series is a random walk; unlikely to find a strategy 
            based on prices alone
        if H > 0.5; the series has a trend; momentum strategies may work

    Parameters
    ----------
    ts : numpy array-like
        array of time series values

    Returns
    -------
    h: float
        Estimate of hurst exponent for time series
    """
    
    #  TODO: test or understand different ranges to check
    # initiate range of lagged values - smaller n may be more accurate
    lags = range(2, 20)

    # calculate the array of variances of lagged differences
    tau = [np.sqrt(np.std(np.subtract(ts[lag:], ts[:-lag]))) for lag in lags]

    # estimate the Hurst exponent
    poly = np.polyfit(np.log(lags), np.log(tau), 1)
    
    # return the Hurst exponent
    return poly[0]*2


def compute_half_life(ts):
    """
    Function for computing the half-life of mean reversion

    Parameters
    ----------
    ts : array-like
        Time series data that we want the half-life of mean reversion for

    Returns
    -------
    lam : float
        lambda, or the half-life of mean reversion for an Ornstein-Uhlenbeck
        process, expressed in units of the time series index

    """
    x = None
    Y = None
    lr = LinearRegression()
    lr.fit(x, Y)
    lam = None
    return lam
    