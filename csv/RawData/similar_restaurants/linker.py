import pandas as pd
import numpy as np

df = pd.read_csv("r.csv")
df = df.values

df_r = pd.read_csv("table1.csv")
df_r = df_r.values

data = []
names = np.array([i if '&amp' not in i else i[:i.index(' &amp')] for i in df_r.T[1]])
for row in df:
	name = row[0]
	index = np.argwhere(names==name)[0][0]
	data.append([df_r[index][0], row[1]])

data = pd.DataFrame(np.array(data))
data.columns = ['restro_id', 'Sim_Restaurant']
data.to_csv("SimilarRestaurant.csv", index=False)