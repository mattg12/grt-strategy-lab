#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
strategy.py

class for building strategies

Author: Matthew Garton
"""
import numpy as np

# TODO: implement OOP framework
class Strategy(object):
    def __init__(self):
        pass
    
    def generate_signals(self, data):
        pass
    
    def apply_trading_rules(self, rule):
        pass
    

def compute_portfolio_pnl(portfolio, data):
    """
    Given a portfolio of positions and data reflecting market prices at the
    beginning and end of the period, compute PnL for the portfolio

    Parameters
    ----------
    portfolio : Portfolio object
        contains information about portfolio holdings at each timestamp
    data : Series
        market data for all securities in portfolio

    Returns
    -------
    pnl : Series
        Change in portfolio value for each time step.
    """
    # TODO: need to figure out code structure first
    for security in portfolio:
        chg = security.position * data.security.change
        portfolio.pnl.append(chg)
    return None


def generate_trade(signal, prices, rules):
    """
    Helper function for turning a signal into a trade, with additional
    parameters applied.

    Parameters
    ----------
    signal : int
        Direction (+/-) and magnitude (TBD) of trading signal
    prices : array-like
        series of prices for security in question
    Returns
    -------
    something : TYPE
        TBD

    """
    # simple concept for trade sizing - strength of signal * min trade size
    trade = signal * rules.unit_size
    
    # add a stop loss if rules dictate
    if rules.stop_loss:
        stop = prices.last - np.sign(signal) * rules.stop_loss
    else:
        stop = None
    
    # decide execution price - assume indiscriminate taker for now
    if 'Bid' in prices.last:
        if trade > 0:
            price = prices.last.Ask
        elif trade < 0:
            price = prices.last.Bid
    else:
        price = prices.last
    
    # TODO: move to separate class - make order ticket object
    ticket = {
        'trade': trade,
        'stop': stop,
        'price': price
        }
    
    return ticket
    
    
    
        


    
    
    