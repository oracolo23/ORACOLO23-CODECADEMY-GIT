
import sqlite3
try:
    connection = sqlite3.connect('feeds_database.db')
    cursor = connection.cursor()
    
    create_table_Query = "CREATE TABLE feed_archive (timestamp TEXT, title TEXT, price TEXT, keepa_link TEXT, img_link TEXT, unique(timestamp, title));"
    cursor.execute(create_table_Query)
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if connection:
        connection.close()
        print("The SQLite connection is closed")



