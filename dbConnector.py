import mysql.connector

scraperDb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="LOL123",
)

dbCursor = scraperDb.cursor()

dbCursor.execute("CREATE DATABASE IF NOT EXISTS jobITListingDB")

dbCursor.execute("CREATE TABLE jobListings (href VARCHAR(255), logo VARCHAR(255), title VARCHAR(255), description VARCHAR(255))")