import pandas as pd
import numpy as np
import mysql.connector

class Cursorer:
	def __init__(self):
		self.i = None
	def execute(self, i):
		self.i = i
mycursor1 = Cursorer()

def delete_tables(mycursor):
	mycursor.execute("DROP TABLE Ratings")
	mycursor.execute("DROP TABLE Menu")
	mycursor.execute("DROP TABLE SimilarRestaurant")
	mycursor.execute("DROP TABLE Contact")
	mycursor.execute("DROP TABLE Restaurant")

def create_tables(mycursor):
	mycursor.execute('''CREATE TABLE Restaurant (
		restro_id INT PRIMARY KEY,
		name VARCHAR(200),
		link VARCHAR(500),
		google_map VARCHAR(500),
		latitude DOUBLE,
		longitude DOUBLE,
		rating FLOAT
	)''')
	mycursor.execute('''CREATE TABLE SimilarRestaurant(
		restro_id INT,
		Sim_Restaurant VARCHAR(500),
		FOREIGN KEY (restro_id) REFERENCES Restaurant(restro_id)
		)''')
	mycursor.execute('''CREATE TABLE Contact(
		restro_id INT,
		c_name VARCHAR(100),
		phone_no VARCHAR(50),
		FOREIGN KEY (restro_id) REFERENCES Restaurant(restro_id)
		)''')
	mycursor.execute('''CREATE TABLE Menu(
		restro_id INT,
		item VARCHAR(500),
		price DOUBLE,
		FOREIGN KEY (restro_id) REFERENCES Restaurant(restro_id)
		)''')
	mycursor.execute('''CREATE TABLE Ratings(
		restro_id INT,
		review VARCHAR(2000),
		profile_name VARCHAR(200),
		delivery_rating DOUBLE,
		dine_in_rating DOUBLE,
		FOREIGN KEY (restro_id) REFERENCES Restaurant(restro_id)
		)''')

def insert_tables(mycursor):
	df = pd.read_csv("./CSVData/restaurant.csv")
	df = df.values
	for row in df:
		mycursor.execute(f"INSERT INTO Restaurant VALUES ({row[0]}, \"{row[1]}\", \"{row[2]}\", \"{row[3]}\", {row[4]}, {row[5]}, {row[6]})")
		print(f"INSERT INTO Restaurant VALUES ({row[0]}, \"{row[1]}\", \"{row[2]}\", \"{row[3]}\", {row[4]}, {row[5]}, {row[6]})")
	df = pd.read_csv("./CSVData/similarRestaurant.csv")
	df = df.values
	for row in df:
		mycursor.execute(f"INSERT INTO SimilarRestaurant VALUES ({row[0]}, \"{row[1]}\")")
		print(f"INSERT INTO SimilarRestaurant VALUES ({row[0]}, \"{row[1]}\")")
	df = pd.read_csv("./CSVData/contact.csv")
	df = df.values
	for row in df:
		mycursor.execute(f"INSERT INTO Contact VALUES ({row[0]}, \"{row[1]}\", \"{row[2]}\")")
		print(f"INSERT INTO Contact VALUES ({row[0]}, \"{row[1]}\", \"{row[2]}\")")
	df = pd.read_csv("./CSVData/menu.csv")
	df = df.values
	for row in df:
		row[1] = row[1].replace("'", " ").replace('"', '')
		mycursor.execute(f"INSERT INTO Menu VALUES ({row[0]}, \"{row[1]}\", {row[2]})")
		print(f"INSERT INTO Menu VALUES ({row[0]}, \"{row[1]}\", {row[2]})")
	df = pd.read_csv("./CSVData/ratings.csv")
	df = df.values
	for row in df:
		mycursor.execute(f"INSERT INTO Ratings VALUES ({row[0]}, \"{row[1]}\", \"{row[2]}\", {row[3]}, {row[4]})")
		print(f"INSERT INTO Ratings VALUES ({row[0]}, \"{row[1]}\", \"{row[2]}\", {row[3]}, {row[4]})")


def create_trigger_and_procedure(mycursor):
	mycursor1.execute('''CREATE TRIGGER InserReviewItem
		AFTER INSERT 
		ON RATINGS FOR EACH ROW
		SELECT 'Thank You for the Review!'
		''')
	mycursor1.execute('''Create PROCEDURE insert_reviewinfo(IN p_restro_id int, IN p_review varchar(2000), IN p_profile_name Varchar(200), IN p_delivery_rating DOUBLE, IN p_dine_in_rating DOUBLE)
    BEGIN
    insert into Ratings(restro_id, review, profile_name, delivery_rating, dine_in_rating) values (p_restro_id, p_review, p_profile_name, p_delivery_rating, p_dine_in_rating);
    END
	''')

if __name__ == '__main__':
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="student",
		database="LabProject"
	)
	mycursor = mydb.cursor()
	delete_tables(mycursor)
	create_tables(mycursor)
	insert_tables(mycursor)
	create_trigger_and_procedure(mycursor)
	mydb.commit()