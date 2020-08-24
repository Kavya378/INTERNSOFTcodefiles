# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:54:30 2020

@author: Kavya
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Superman = pd.read_csv('AAPL Historical Data.csv' ,usecols=[0,1,2,3,4])

POHL_avg=Superman[['Price','Open','High','Low']].mean(axis=1)

obs=np.arange(1,len(Superman)+1,1)

plt.plot(obs,POHL_avg,'r',label='MY FIRST PLOT')