import streamlit as st
import pandas as pd
import numpy as np
import re

def remove_x(string):
	string1 = ''
	i = 0
	while(i<len(string)):
		try:
			if string[i]=='\\' and string[i+1]=='x':
				i+=4
			else:
				string1 += string[i]
				i+=1
		except:
			pass
	return string1

def app(restaurants, option, names):
	restro_id_selected = names.index(option)
	st.title("Reviews & Ratings - "+option)
	if restaurants[restro_id_selected][6]!=-1:
		st.markdown("#### Overall Rating:- "+str(restaurants[restro_id_selected][6]))
	reviews = pd.read_csv("./Data/ratings.csv")
	reviews = reviews.values
	review_items = [i for i in reviews if i[0]==restaurants[restro_id_selected][0]]
	if len(review_items)>0:
		st.markdown('##### Most Recent Reviews:')
		review_items = np.array(review_items)
		review_items.T[-1] = [str(i) if i!=-1 else '' for i in review_items.T[-1]]
		review_items.T[-2] = [str(i) if i!=-1 else '' for i in review_items.T[-2]]
		review_items = review_items.T[1:].T
		temp = review_items.T[0].copy()
		review_items.T[0] = review_items.T[1]
		review_items.T[1] = [i if str(i)!='nan' else '' for i in temp]
		review_items.T[1] = [remove_x(i) for i in review_items.T[1]]
		review_items = pd.DataFrame(review_items)
		review_items.columns = ['Profile Name', 'Description', 'Delivery Ratings', 'Dine-In Ratings']
		review_items.set_index('Profile Name', inplace=True)
		st.dataframe(review_items)
	else:
		st.error("No Ratings Recorded Yet!")