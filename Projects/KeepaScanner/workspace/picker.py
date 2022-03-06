
import pandas as pd
import feedparser
import csv
import os.path
import time
from os import path


def feed_reader():
    NewsFeed = feedparser.parse("https://dyn.keepa.com/v2/user/rss/?feed=2u9m3j720a4r195m0rbahnc8e45nlab4")
        #list of new feeds
    current_entry = NewsFeed.entries
    feed_lenght = len(current_entry)
    # define a index to start from new feeds. it should be timestamp based
    starting_index = 0 
    if path.exists("output.csv") == False:
        print("file does not exists, generating it ...")
        time.sleep(10)
        with open("output.csv", 'w', newline = "") as output:
            fieldnames = ["timestamp", "title", "price", "keepa_link", "img_link"]    
            writer = csv.DictWriter(output, fieldnames = fieldnames)  
            writer.writeheader()
            print("file generated, starting indexing")
            time.sleep(10)

            print("feed currently contains: " + str(feed_lenght))
            time.sleep(5)
    for entry in current_entry[starting_index:]:
            new_items = []            
            new_item = {}
            feed_title = NewsFeed.entries[starting_index]["title"]
            new_feed_title = feed_title.replace(",", "")
            feed_description = NewsFeed.entries[starting_index]["description"]
            new_feed_description = feed_description.replace(",", "")
            feed_published = NewsFeed.entries[starting_index]["published"]
            new_feed_published = feed_published.replace(",", "")
            try :
                money_index = new_feed_description.index("€")
                    
            except ValueError:
                money_index = new_feed_description.index("£") 
            price = new_feed_description[money_index:]
            keepa_link = current_entry[starting_index]["links"][0]["href"]    
            img_link = current_entry[starting_index]["links"][1]["href"]
                #assigning values to new item dict
            new_item["timestamp"] = new_feed_published
            new_item["title"] = new_feed_title
            new_item["price"] = price
            new_item["keepa_link"] = keepa_link
            new_item["img_link"] = img_link
                
            print("NEW ITEM DETECTED")
            print(str(new_feed_title[:30]))
            print(str(new_feed_published))
            print(str(price))
            print(str(starting_index))
            print("\n")
                
            new_items.append(new_item)                   
            starting_index+=1
            
            with open("output.csv", 'a' ) as output:
                fieldnames = ["timestamp", "title", "price", "keepa_link", "img_link"]
                writer = csv.DictWriter(output, fieldnames = fieldnames)
                for items in new_items:
                    writer.writerow(items)
                    
                    
                    




                      
                        
                    
         
    
                  
    

    

        

