import pandas as pd
import numpy as np

df = pd.read_csv("Scraped_Restaurants.csv")
df = df.values
names = df.T[0]
links = df.T[1]
loc = pd.read_csv("links.csv")
loc = loc.values
loc_names = [i.strip() for i in loc.T[0]]
location_links = []
for name in [n.strip() for n in names]:
	index = -1
	try:
		index = loc_names.index(name)
	except:
		index = loc_names.index(name[:name.index('&amp;')-1])
	if index!=-1:
		location_links .append(loc.T[1][index])
	else:
		location_links.append("")
#print(location_links)
lat_long = [[float(j) for j in i[i.index('destination=')+len('destination='):].split(',')] for i in location_links]
lat = [i[0] for i in lat_long]
long = [i[1] for i in lat_long]
print(len(names), len(links), len(location_links), len(lat), len(long))
combined = np.array([[i for i in range(len(names))], [i for i in names], [i for i in links], location_links, lat, long])
combined = pd.DataFrame(combined.T)
combined.columns = ['restro_id', 'names', 'links', 'Google-Maps Links', 'Latitude', 'Longitude']
combined.to_csv('table1.csv', index=False)