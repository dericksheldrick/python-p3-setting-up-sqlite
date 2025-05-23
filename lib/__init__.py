import sqlite3

#connection string- a statement that allow you to connect the database. 
# It also define the details of the database 
# - path(url),database_name,username,password
# cursor - used to do somethig 

connection = sqlite3.connect('lib/clinic_dabase.db')
cursor = connection.cursor()