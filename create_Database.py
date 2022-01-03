# =================================================================== #
# Module        : Data Representation
# Author        : Martina O'Brien - G00376463
# Description   : Python to create a Database in Mysql 
# File Name     : create_Database.py
# =================================================================== #

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
)

# Setting up SQL for mysql to create database
cursor = db.cursor()
cursor.execute("CREATE DATABASE datarepresentation6")

print("###### Your Database is ready for use ########")