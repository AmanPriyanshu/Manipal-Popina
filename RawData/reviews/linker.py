import pandas as pd
import numpy as np
import random

df = pd.read_csv("r.csv")
df = df.values

df_r = pd.read_csv("table1.csv")
df_r = df_r.values

data = []
names = np.array([i if '&amp' not in i else i[:i.index(' &amp')] for i in df_r.T[1]])
for row in df:
	name = row[0]
	index = np.argwhere(names==name)[0][0]
	if random.random()<0.2:
		data.append([df_r[index][0], row[2], row[1], -1, row[3]])
	else:
		data.append([df_r[index][0], row[2], row[1], row[3], -1])

data = pd.DataFrame(np.array(data))
data.columns = ['restro_id', 'review', 'profile_name', 'delivery_rating', 'dine_in_rating']
data.to_csv("Ratings.csv", index=False)