import streamlit as st
import pandas as pd
import numpy as np

def app(restaurants, option, names):
	restro_id_selected = names.index(option)
	st.title("Menu - "+option)
	menu = pd.read_csv("./Data/menu.csv")
	menu = menu.values
	st.markdown("#### Menu:")
	menu_items = [i for i in menu if i[0]==restaurants[restro_id_selected][0]]
	col1,col2 = st.columns([3,1])
	with col1:
		for item in menu_items:
			st.warning(item[1])
	with col2:
		for item in menu_items:
			st.success(item[2])
	if len(menu_items)==0:
		st.error("No Menu Available")