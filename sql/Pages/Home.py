import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import numpy as np

@st.cache(hash_funcs={folium.folium.Map: lambda _: None}, allow_output_mutation=True)
def make_map(df, display_all=True):
	if display_all:
		main_map = folium.Map(location=(13.3440134, 74.784465), zoom_start=15)
		for row in df:
			folium.Marker(location=[float(row[-3]), float(row[-2])],
				tooltip=f"{row[1]}",
				fill=True,
				fill_color="blue",
				color=None,
				fill_opacity=0.7,
				radius=5,
			).add_to(main_map)
	else:
		main_map = folium.Map(location=(float(df[-3]), float(df[-2])), zoom_start=16)
		folium.Marker(location=[float(df[-3]), float(df[-2])],
			tooltip=f"{df[1]}",
			fill=True,
			fill_color="blue",
			color=None,
			fill_opacity=0.7,
			radius=5,
		).add_to(main_map)
	return main_map

def app(placeholder_map, restaurants, names, option, mycursor):
	if True:
		restro_id_selected = names.index(option)
		with placeholder_map.container():
			main_map = make_map(restaurants[restro_id_selected], False)
			folium_static(main_map)
		placeholder_menu = st.empty()
		with placeholder_menu.container():
			st.markdown('#### Ordering Link:')
			st.write('[LINK]('+restaurants[restro_id_selected][2]+')')
			mycursor.execute("SELECT t.c_name, t.phone_no FROM (SELECT * FROM Contact WHERE restro_id="+str(restaurants[restro_id_selected][0])+") AS t")
			contacts = mycursor.fetchall()
			contacts = [[j for j in i] for i in contacts]
			contact_items = contacts
			st.markdown("#### Contacts:")
			for contact in contact_items:
				st.info(contact[0]+':-&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+91 '+str(contact[1])[2:])
			if len(contact_items)==0:
				st.error("No Contacts")
			mycursor.execute("SELECT * FROM SimilarRestaurant WHERE restro_id="+str(restaurants[restro_id_selected][0]))
			similar_items = mycursor.fetchall()
			similar_items = [[j for j in i] for i in similar_items]
			if len(similar_items)>0:
				st.markdown("#### Similar Restaurants")
				for index, similar in enumerate(similar_items):
					r_name = str(similar[1]).replace('https://www.zomato.com/manipal/', '').replace('-', ' ')
					r_name = ' '.join([i[0].upper()+i[1:] if len(i)>1 else i.upper() for i in r_name.split()])
					st.markdown('[Restaurant: '+r_name+']('+str(similar[1])+')')