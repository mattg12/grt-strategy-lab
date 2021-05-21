#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_data_ingestion.py

script for testing data ingestion functions

Author: Matthew Garton
"""

# TODO: build out test
from utils.data_ingestion import (
    get_stock_prices,
    get_forex_prices,
    get_crypto_prices
    )

stocks = get_stock_prices('SPY', 'av')
fx = get_forex_prices('EUR', 'USD', 'av')
crypto = get_crypto_prices('BTC', 'USD', 'av')
    