import streamlit as st
import pandas as pd
import numpy as np

def app(restaurants, option, names, mycursor):
	restro_id_selected = names.index(option)
	st.title("Menu - "+option)
	mycursor.execute("SELECT * FROM Menu WHERE restro_id="+str(restaurants[restro_id_selected][0]))
	menu = mycursor.fetchall()
	menu_items = [[j for j in i] for i in menu]
	st.markdown("#### Menu:")
	col1,col2 = st.columns([3,1])
	with col1:
		for item in menu_items:
			st.warning(item[1])
	with col2:
		for item in menu_items:
			st.success(item[2])
	if len(menu_items)==0:
		st.error("No Menu Available")