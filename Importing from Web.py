# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 19:53:52 2018

@author: Jack Chung
"""

# Import these for convenience even if might not need all of them
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

import urllib
import urllib.request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests

#================================================================
#****************************************************************
# Extract HTML from a webpage using "urllib" package
# Import the necessary functions
from urllib.request import urlopen, Request
# Assign the url
url = 'https://www.wikipedia.org/'
# Send the GET request
request = Request(url)
# Catach the response using urlopen(), which returns a html object
response = urlopen(request)
# apply .read method which returns the HTML as a string stored in variable "html"
html = response.read()
# Finally be polite and close the response
response.close()

#================================================================
#****************************************************************

# Extract HTML from a webpage using the "Requests" Package
# Import the package
import requests
# Assign the url
url = 'https://www.wikipedia.org/'
# Package, send and patch the response with a single function "requests.get()"
r = requests.get(url)
# Apply .text method to the response,r, to return the HTML as a string
html = r.text

#================================================================
#****************************************************************

# Analyse HTML using BeautifulSoup
# Load package "BeautifulSoup", and package "requests"
from bs4 import BeautifulSoup
import requests
# Now scrape HTML from wikipedia homepage
url = 'https://www.wikipedia.org/'
r = requests.get(url)
html_doc = r.text
# Create a beautifulsoup object and then prettify it
soup = BeautifulSoup(html_doc)
print(soup.prettify())

# Some more soup.methods
print(soup.title)
print(soup.get_text())

# Extract all hyperlinks from web page
for link in soup.find_all('a'): print(link.get('href'))

#================================================================
#****************************************************************

# Scrap Donald Trump Twitter page

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = make_soup("https://twitter.com/realDonaldTrump")

# To check we have the correct page
print(soup.title) 

# Find all 'a' tags
print(soup.findAll('a')) 

# Find all 'href' in 'a' tags
for link in soup.findAll('a'):
    print(link.get('href'))   # or print(link.text)

# In 'div' class, locate "ProfileHeaderCard" class
print(soup.find('div', {"class":"ProfileHeaderCard"}))
# In 'div' class, locate "ProfileHeaderCard" class, and within that locate "p" class's text 
print(soup.find('div', {"class":"ProfileHeaderCard"}).find('p').text)


# To get all the tweets from Donald Trump without indexing
for tweets in soup.findAll('div', {"class":"content"}):
    print(tweets.find('p').text)

# To get all the tweets from Donald Trump with indexing
i =1
for tweets in soup.findAll('div', {"class":"content"}):
    print(i)
    print(tweets.find('p').text)
    i = i+1

#================================================================
#****************************************************************

# Scrape Table Data from Website

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = make_soup("https://www.basketball-reference.com/players/a/")
print(soup.title) 

# Next we loop through each of the rows and data
playerdatasaved=""
soup = make_soup("https://www.basketball-reference.com/players/a/")
for record in soup.findAll('tr'):
    playerdata=""  # reset the counter
    for data in record.findAll('td'):
        playerdata = playerdata + "," + data.text
    playerdatasaved = playerdatasaved + "\n" + playerdata[1:]
print(playerdatasaved)
          
# Save the playerdatasaved as .csv in current working directory
file = open(os.path.expanduser("Basketball.csv"), "wb")   
file.write(bytes(playerdatasaved, encoding="ascii", errors='ignore'))
 # The Basketball.csv was created in the cwd but I couldn’t transform it to
 # dataframe using pandas because the elements in the table didn’t match as
 # some players had 2 colleges instead of 1


#================================================================
#****************************************************************

# Scrape Yahoo Finance Stock Ticker Data, grab multiple ticker info
import urllib
import urllib.request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests
import pandas as pd

labels=[]
data=[]
tickers=['AAPL', 'MMM', 'T', 'S', 'VZ']

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

for ticker in tickers:
    url = 'https://finance.yahoo.com/quote/'+ticker+'?p='+ticker
    soup = make_soup(url)
    table = soup.find('div', id='quote-summary')
    rows = table.findAll('tr')
    for row in rows:
        labels.append(str(row.find_all('td')[0].text+' '+ ticker))
        data.append(str(row.find_all('td')[1].text))
    cols = {'Fields':labels, 'Data':data}
df=pd.DataFrame(cols)
df.to_csv('ticker.csv')  











