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

def app(placeholder_map, restaurants, names, option):
	if True:
		restro_id_selected = names.index(option)
		with placeholder_map.container():
			main_map = make_map(restaurants[restro_id_selected], False)
			folium_static(main_map)
		placeholder_menu = st.empty()
		with placeholder_menu.container():
			st.markdown('#### Ordering Link:')
			st.write('[LINK]('+restaurants[restro_id_selected][2]+')')
			contacts = pd.read_csv("./Data/contact.csv")
			contacts = contacts.values
			contact_items = [i for i in contacts if i[0]==restaurants[restro_id_selected][0]]
			st.markdown("#### Contacts:")
			for contact in contact_items:
				st.info(contact[1]+':-&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+91 '+str(contact[2])[2:])
			if len(contact_items)==0:
				st.error("No Contacts")
			similars = pd.read_csv('./Data/similarRestaurant.csv')
			similars = similars.values
			similar_items = [i for i in similars if i[0]==restaurants[restro_id_selected][0]]
			if len(similar_items)>0:
				st.markdown("#### Similar Restaurants")
				for index, similar in enumerate(similar_items):
					r_name = str(similar[1]).replace('https://www.zomato.com/manipal/', '').replace('-', ' ')
					r_name = ' '.join([i[0].upper()+i[1:] if len(i)>1 else i.upper() for i in r_name.split()])
					st.markdown('[Restaurant: '+r_name+']('+str(similar[1])+')')