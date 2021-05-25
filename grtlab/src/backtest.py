#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
backtest.py 

Define classes required for backtesting an algorithmic trading strategy.

@author: mattg
"""

class Strategy:
    def __init__(self, symbols):
        self.symbols = symbols
        

    def generate_signals(self):
        pass
    

class Portfolio:
    def __init__(self)