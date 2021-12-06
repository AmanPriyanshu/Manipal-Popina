import pandas as pd
import numpy as np

df = pd.read_csv("table1.csv")
df = df.values

df_r = pd.read_csv("ratings.csv", header=None)
df_r = df_r.values

ds = []
for row in df:
	name = row[1]
	if '&amp' in name:
		name = name[:name.index('&amp')-1]
	try:
		index = np.argwhere(df_r.T[0]==name)[0][0]
		ds.append([i for i in row]+[df_r[index][-1]])
	except:
		ds.append([i for i in row]+[-1])
ds = pd.DataFrame(np.array(ds))
ds.to_csv("ds.csv", index=False)