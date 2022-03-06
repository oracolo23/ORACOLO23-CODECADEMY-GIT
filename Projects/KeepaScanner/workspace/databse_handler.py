
import sqlite3
import os
import pandas as pd

def db_handler():
    current_archive = pd.read_csv("output.csv", sep=',')
    current_archive_list = current_archive.iterrows()
    print("current feed length is:" + str(len(current_archive)))
    print(current_archive)
    for items in current_archive_list:
  
        try:
            connection = sqlite3.connect('feeds_database.db')
            cursor = connection.cursor()
            print("Successfully Connected to SQLite")
            query = """INSERT INTO feed_archive VALUES (?, ?, ?, ?, ?);"""     
            cursor.execute(query, items[1])
            print("New Feed added to Database")
            connection.commit()
        except sqlite3.IntegrityError:
            print("Item with same [timestamp] and [title] already exists, skipping item.")
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
        
            

    cursor.close()
    connection.close()
    print("The SQLite connection is closed")
    os.remove('output.csv')
    print("Current scan deleted, restarting scan")