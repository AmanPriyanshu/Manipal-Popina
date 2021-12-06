import streamlit as st
from Pages import Home, About_App, Reviews, Menu, Team
from Pages.Home import make_map
from streamlit_folium import folium_static
import folium
import pandas as pd
import mysql.connector
from make_sql import delete_tables, create_tables, insert_tables

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="student",
  database="LabProject"
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
	if st.sidebar.button('Explore'):
		Home.app(placeholder_map, restaurants, names, option, mycursor)
	if st.sidebar.button('Menu'):
		emp.empty()
		Menu.app(restaurants, option, names, mycursor)
	if st.sidebar.button('Reviews & Ratings'):
		emp.empty()
		Reviews.app(restaurants, option, names, mycursor)
	if st.sidebar.button('About App'):
		emp.empty()
		About_App.app()
	if st.sidebar.button('Team'):
		emp.empty()
		Team.app()


if __name__ == '__main__':
	app()