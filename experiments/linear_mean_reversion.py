#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
linear_mean_reversion.py

script for implementing a simple linear mean reverting strategy on a single
asset strategy: set position equal to the negative normalized deviation from
its moving average

credit: 'Algorithmic Trading: Winning Strategies and their Rationale' by 
Ernest P. Chan (2013)

Author: Matthew Garton
"""
import numpy as np
import matplotlib.pyplot as plt
from utils.data_ingestion import get_forex_prices
from utils.mean_reversion import compute_half_life
# choose currency pair
base_cur = 'CAD'
price_cur = 'USD'

# choose start and end dates
start_date = '2007-07-22'
end_date = '2012-03-28'

# get data
usd_cad = get_forex_prices(base_cur, price_cur, source='av')

# slice data to desired timescale
training_data = usd_cad[:start_date]
backtest_data = usd_cad.loc[start_date: end_date]

# compute lambda, the half-life of mean-reversion
# TODO: write half life computation formula in utils

# apply a simple linear mean reversion strategy to USDCAD
lookback = int(np.round(compute_half_life(training_data['close'])))
y = backtest_data[['close']]

# TODO: import or write methods to compute MA and MSTD
position = - (y - y.rolling(lookback).mean()) / y.rolling(lookback).std()
pnl = position.shift() * y.pct_change() # TODO: method for computing strategy PnL
equity = np.cumsum(pnl)

# TODO: write own methods for: strategy, position, p&L

# view equity curve
plt.plot(equity)
plt.show()

# TODO: method for tearsheet w/ backtest statistics