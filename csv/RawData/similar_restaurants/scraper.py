import os
import sys
import pandas as pd
import numpy as np

df = pd.read_csv('table1.csv')
df = df.values
names = df.T[1]
links = df.T[2]
for name, link in zip(names, links):
	os.system('python ranking_scraper.py '+link.replace('/order', '')+' '+name)