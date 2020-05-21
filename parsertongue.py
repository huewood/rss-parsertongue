## Import libraries
import feedparser
from tabulate import tabulate
import time
from datetime import date
# Todays date
#today = date.today
# Test date
today = "2020-05-14"
#print(today)

## Variable declarations
# Set the RSS URL
url= "https://alas.aws.amazon.com/alas.rss"
# Create empty arrays for the XML elements
title_list = []
link_list = []
# Define headers for table output
headers  = ["Title","Link"]

## RSS Parsing
feed = feedparser.parse(url)
# For each item in the feed, put the relevant element into array
for item in feed.entries:
    date = "%d-%02d-%02d" % (item.published_parsed.tm_year, \
            item.published_parsed.tm_mon, \
            item.published_parsed.tm_mday)
    if date == today:
        title_list.append(item.title)
        link_list.append(item.link)

# Create table variable with zipped element lists
table = zip(title_list, link_list)
# Print table using tabulate library
print(len(title_list), "patch(es) came out on", today,":")
print(tabulate(table, headers=headers))

# Debugging
print("Total RSS items:", len(feed.entries))