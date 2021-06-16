#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gdp_db_test.py

Testing connection to Google Cloud Platform SQL Database
Created on Tue Jun 15 21:25:18 2021

@author: mattg
"""
from google.cloud.sql.connector import connector
from configparser import ConfigParser

config = ConfigParser()
config.read('./config/smdb.conf')
instance = config['connector_python']['instance']
usr = config['connector_python']['user']
pword = config['connector_python']['password']
database = config['connector_python']['database']

conn = connector.connect(
    instance_connection_string=instance,
    driver='pymysql',
    user=usr,
    password=pword,
    db=database
    )

# test by executing a query
cur = conn.cursor()
cur.execute('SELECT * FROM vendors')

# fetch results
res = cur.fetchall()

# print results
for row in res[:10]:
    print(row)
    
conn.close()
