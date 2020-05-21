## Import libraries
import feedparser
from tabulate import tabulate

## Variable declarations
# Set the RSS URL
url= "https://alas.aws.amazon.com/alas.rss"
# Create empty arrays for the XML elements
date_list = []
title_list = []
link_list = []
# Define headers for table output
headers  = ["Date","Title","Link"]

## RSS Parsing
feed = feedparser.parse(url)
# For each item in the feed, put the relevant element into array
for item in feed.entries:
    date = "(%d/%02d/%02d)" % (item.published_parsed.tm_year, \
        item.published_parsed.tm_mon, \
        item.published_parsed.tm_mday)
    date_list.append(date)
    title_list.append(item.title)
    link_list.append(item.link)

# Create table variable with zipped element lists
table = zip(date_list, title_list, link_list)
# Print table using tabulate library
print(tabulate(table, headers=headers))

print("Number of total RSS items:", len(feed.entries))