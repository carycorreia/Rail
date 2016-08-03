# Project:  GE Rail Short Line Identifier - From an article site
# Scope:    Program to find and scrape demand gen data from US Utilities
#           - This program grabs all utility data generated from Part I
# Date:     July 27, 2016
# Analyst:  Cary Correia
###########################################################################
#
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pandas as pd
import os
import sqlite3
import sqlalchemy

def quote(s1):
    return "'{}'".format(s1)

# setup path for this project
path = "/Users/carycorreia/Documents/Projects/GE Stuff/Rail"
os.chdir(path)
#
# input all of Part I's utilities and utility links
conn = sqlite3.connect('US_Railroads')
cur = conn.cursor()

###########################################################################
#
cur.execute('''
DROP TABLE IF EXISTS US_Short_line_RR''')

cur.execute('''
CREATE TABLE US_Short_line_RR (company TEXT, source Text)''')

# Setup target url for scraper
site = "http://www.american-rails.com/short-line-railroad-guide.html"
htmlfile =urlopen(site)
soup = BeautifulSoup(htmlfile.read(), "html.parser")

    # grab table with reference
rails = soup.find_all("p")
i=1
for company in rails:
    try:
        short = company.find("em").getText()
        source = "http://www.american-rails.com/short-line-railroad-guide.html"
        i=i+1
        # add to SQL Firmo DB
        cur.execute('''INSERT INTO US_Short_line_RR (company, source ) VALUES (?,?)''', (short, site,))
        conn.commit()
    except:
        continue














