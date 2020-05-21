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

for post in feed.entries:
    date = "(%d/%02d/%02d)" % (post.published_parsed.tm_year, \
        post.published_parsed.tm_mon, \
        post.published_parsed.tm_mday)
    date_list.append(date)
    title_list.append(post.title)
    link_list.append(post.link)

table = zip(date_list, title_list, link_list)
print(tabulate(table, headers=headers))

print("Number of total RSS posts:", len(feed.entries))