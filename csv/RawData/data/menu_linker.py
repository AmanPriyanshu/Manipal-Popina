import pandas as pd
import numpy as np
import os

files = os.listdir("./restros/")
df = pd.read_csv("table1.csv")
df = df.values
names = [i if '&amp' not in i else i[:i.index(' &amp')] for i in df.T[1]]
names = np.array([i.replace(' ', '_')+'.csv' for i in names])
menu_df = []
for file in files:
	index = np.argwhere(names==file)[0][0]
	r_id = df[index][0]
	ds = pd.read_csv('./restros/'+file)
	ds = ds.values
	for row in ds:
		menu_df.append([r_id]+[i for i in row])

menu_df = pd.DataFrame(np.array(menu_df))
menu_df.columns = ['restro_id', 'item', 'price']
menu_df.to_csv("menu.csv", index=False)