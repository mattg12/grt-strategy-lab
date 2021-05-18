# grt-strategy-lab

Repository for quantitative research and development of algorithmic trading strategies

## Description

This project is intended to serve as a lightweight, all-purpose research lab for quantitative trading, including all of the tools and infrastructure to explore financial data, test a hypothesis, and backtest a strategy.  

## Table of Contents

1. [Getting Started](#getting-started)
2. [Directory](#project-directory)
3. [About the Author](#about-the-author)
4. [Acknowledgments](#acknowledgments)
5. [Resources](#resources)

## Getting Started

### Dependencies & Prerequisites

* Full dependencies will be added at a later date
* Personally, I am running the following:
  * Python 3.8.5+
    *  Packages as listed in `requirements.txt`
  * Ubuntu 18.04.4+

### Installing

* Full installation instructions to be added at a later date
* You will need your own API Keys (or alternate data sources) for any data used

## Project Directory


Repository Structure (adapted from [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)

```
grt-strategy-lab/
├── README.md          
├── data/
│   ├── external/      
│   ├── interim/       
│   ├── processed/     
│   └── raw/           
│
├── docs/              
│
├── algos/             
│
├── notebooks/         
│
├── references/        
│
├── reports/           
│   └── figures/       
│
├── requirements.txt   
│                         
├── setup.py           
├── src/               
    ├── __init__.py    
    │
    ├── data/          
    │   └── make_dataset.py
    │
    ├── features/      
    │   └── build_features.py
    │
    ├── utils/
    |   └── helpers.py
    |
    ├── algos/        
    │   │                 
    │   ├── predict_model.py
    │   └── train_model.py
    │
    └── visualization/ 
        └── visualize.py
```  

## About the Author

[Matthew Garton](https://www.linkedin.com/in/matt-garton/) is a quantitative trader with over 8 years of experience in financial markets as an options market maker, a buy side trader, and more recently as an independent trader and researcher. His primary areas of interest for research include volatility, options strategies, and commodities.


## Acknowledgments

TBD

## Resources
