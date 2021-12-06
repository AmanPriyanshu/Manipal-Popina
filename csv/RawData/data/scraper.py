import os
import sys
import pandas as pd
import numpy as np

df = pd.read_csv('Scraped_Restaurants.csv')
df = df.values
names = df.T[0]
links = df.T[1]
for name, link in zip(names, links):
	os.system('python ranking_scraper.py '+link+' '+name)