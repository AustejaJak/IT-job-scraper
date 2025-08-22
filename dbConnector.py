import mysql.connector

scraperDb = mysql.connector.connect( # put info to env
    host="localhost",
    user="root",
    passwd="LOL123",
)

dbCursor = scraperDb.cursor()

dbCursor.execute("CREATE DATABASE IF NOT EXISTS jobITListingDB")

dbCursor.execute("CREATE TABLE IF NOT EXISTS jobListing (href VARCHAR(255), logo VARCHAR(255), title VARCHAR(255), salary_amount VARCHAR(255), salary_calculation VARCHAR(255), location VARCHAR(255), posted VARCHAR(255))")

sql = "INSERT INTO JobListing (href, logo, title, salary_amount, salary_calculation, location, posted) VALUES (%s, %s, %s, %s, %s, %s, %s)"

