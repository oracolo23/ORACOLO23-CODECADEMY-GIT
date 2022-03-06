
import pandas as pd
import schedule
import time
import picker
import databse_handler



        
schedule.every(3).minutes.do(picker.feed_reader)
time.sleep(5)
schedule.every(3).minutes.do(databse_handler.db_handler)

while True:
    schedule.run_pending()
    print("****  SEARCHING ...   ****")
    
        
           
    time.sleep(5)
