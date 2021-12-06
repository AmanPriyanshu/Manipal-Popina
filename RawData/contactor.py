import pandas as pd
import numpy as np

df = pd.read_csv("numbers.csv")
df = df.values
df_r = pd.read_csv("table1.csv")
df_r = df_r.values
names = np.array([i if '&amp' not in i else i[:i.index(' &amp')] for i in df_r.T[1]])
ds = []
for row in df:
	name = row[0]
	r_id = np.argwhere(names==name)[0][0]
	numbers = row[1].split(',')
	for n_id, number in enumerate(numbers):
		ds.append([df_r[r_id][0], 'Contact'+str(n_id+1), number.strip()])
ds = pd.DataFrame(np.array(ds))
ds.columns = ['restro_id', 'c_name', 'phone_no']
ds.to_csv("contact.csv", index=False)