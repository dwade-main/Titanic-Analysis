# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 06:13:31 2021

@author: ghost
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create dataframe using .csv, print to verify
titanic_df = pd.read_csv('passenger_data.csv')
print(titanic_df.head())

