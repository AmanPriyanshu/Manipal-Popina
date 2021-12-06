import streamlit as st

def app():
	st.title("About App")
	st.image('home.jpg')
	st.markdown('''
		We propose an applet that curates the name of the restaurant, location, and the menu of the restaurant. To aid customer perception we also provide the ratings of each restaurant. We first found there to be a total of 167 restaurants upon surveying multiple websites such as Zomato, Google, etc. We used Python’s Scrapy library for aggregating real-time data. We utilized geographical pinpointing for selecting these places. Their menu items, ratings, location details, etc. were recovered from these sources. We modularized our code to scrape for user-sourced locations focusing on Manipal for said project. This allowed us to use real-life data in our project aggregated over trusted sources. 

An aggregate of 168 restaurants were applicable for our localization function, scraping these restaurants allowed us to complete our database with real data. Ratings of over 62 restaurants are provided, with an average of 4.22/5 stars. Location of each restaurant was addressed using Google Maps and appropriate links are presented through our project. We were able to survey and agglomerate the menu details of 141 restaurants, with an average of 63 items available in each of these. 
		''')