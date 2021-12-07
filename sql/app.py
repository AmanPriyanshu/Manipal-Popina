# CREATE DATABASE labp;
# USE labp;

import streamlit as st
from Pages import Home, About_App, Reviews, Menu, Team
from Pages.Home import make_map
from streamlit_folium import folium_static
import folium
import pandas as pd
import mysql.connector
from make_sql import delete_tables, create_tables, insert_tables

res1 = "Thank You for the Review!"
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="student",
  database="labp"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT name FROM Restaurant")
names = [str(i[0]) for i in mycursor.fetchall()]
mycursor.execute("SELECT * FROM Restaurant")
restaurants = [[j for j in i] for i in mycursor.fetchall()]		

def app():
	global mycursor
	st.sidebar.image('logo.png', use_column_width=500, width=300)
	st.sidebar.title("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAVIGATION")
	st.markdown("""
		<style>
		div.stButton > button:first-child {
		height:3em;width:18em;border-radius:10px 10px 10px 10px;
		}
		</style>
	""", unsafe_allow_html=True)
	emp = st.empty()
	with emp.container():
		st.title("Order From The Best Restaurants Near You!")
		placeholder_map = st.empty()
		with placeholder_map.container():
			main_map = make_map(restaurants)
			folium_static(main_map)
		option = st.selectbox("Select Your Restaurant!", names)
		restro_id_selected = names.index(option)
		restro_id = restaurants[restro_id_selected][0]
	emp_rev = st.empty()
	with emp_rev.container():
		st.markdown("# Enter A Review!")
		user_profile = st.text_input("Enter Profile Name:")
		review = st.text_area("Review", '''The food was some of the b....
			''', height=3)
		rating = st.number_input("Enter rating:", 0, 5, step=1)
		rating_type = st.radio("Enter Rating Type:", ('Delivery', 'Dine-In'))
		if st.button("SUBMIT"):
			if rating_type=='Delivery':
				mycursor.execute(f'CALL insert_reviewinfo({restro_id}, \"{review}\", \"{user_profile}\", {rating}, -1)')
			else:
				mycursor.execute(f'CALL insert_reviewinfo({restro_id}, \"{review}\", \"{user_profile}\", -1, {rating})')
			mydb.commit()
			res = mycursor.fetchall()
			st.success(res1)

	if st.sidebar.button('Explore'):
		Home.app(placeholder_map, restaurants, names, option, mycursor)
		emp_rev.empty()
	if st.sidebar.button('Menu'):
		emp.empty()
		Menu.app(restaurants, option, names, mycursor)
		emp_rev.empty()
	if st.sidebar.button('Reviews & Ratings'):
		emp.empty()
		Reviews.app(restaurants, option, names, mycursor)
	if st.sidebar.button('About App'):
		emp.empty()
		About_App.app()
		emp_rev.empty()
	if st.sidebar.button('Team'):
		emp.empty()
		Team.app()
		emp_rev.empty()

if __name__ == '__main__':
	app()