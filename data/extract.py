import pandas as pd
import numpy as np

with open('full_zomato.txt', mode="r", encoding="utf-8") as f:
	details = f.readlines()
details = [i.strip() for i in details if i.strip() != '']
details = ' '.join([details[3], details[5]])
details = details.split('<a href="/manipal/')[13:]
links, names = [], []
for i, val in enumerate(details):
	if i%2==1:
		try:
			link = 'https://www.zomato.com/manipal/'+val[:val.index('" class="')]
			name = val[val.index('"><h4 class="')+len('"><h4 class="'):]
			name = name[name.index('">')+2:name.index('</h4><div class="')]
			links.append(link)
			names.append(name)
		except:
			pass
df = pd.DataFrame({'names': names, 'links': links})
df.to_csv("Scraped_Restaurants.csv", index=False, mode='a')