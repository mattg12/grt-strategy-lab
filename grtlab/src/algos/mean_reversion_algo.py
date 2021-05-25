#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:27:15 2021

@author: mattg
"""
from logging import Logger
from backtest import Strategy


class MeanReversionAlgorithm(Strategy):
    def generate_signals():
        pass
    
if __name__ == 'main':
    
    log = Logger()
    # TODO: query for required data
    
    # TODO: generate signals from data based on rule
    
    # TODO: instantiate a portfolio
    
    # TODO: generate trades based on signals and risk management parameters
    
    # TODO: generate and print backtest statistics + equity curve
    log.debug("BACKTEST COMPLETE")