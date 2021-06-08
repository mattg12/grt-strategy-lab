#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
strategy.py

class for building strategies

Author: Matthew Garton
"""

class Strategy(object):
    def __init__(self):
        pass
    
    def generate_signals(self, data):
        pass
    
    def apply_trading_rules(self, rule):
        pass
    

def TrailingStop(Strategy):
    
    # logic
    def enter_position(self, data):
        if self.position == 0 and abs(self.signal) > self.threshold:
            self.position = self.signal * self.symbol.trade_size
            self.stop = self.symbol.price - self.signal * self.stop_loss_target
    
    def update_stop(self, data):
        pass
    
    def exit_position(self, data):
        pass
    

def PortfolioWeights(Strategy):
    pass
        


    
    
    