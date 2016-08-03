# Project:  GE Rail Short Line Identifier - From ASLRRA
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
DROP TABLE IF EXISTS US_Short_line_RR_II''')

cur.execute('''
CREATE TABLE US_Short_line_RR_II (name TEXT, website Text)''')

# Setup target url for scraper
site = "https://www.aslrra.org/web/Members/Directory/web/Dir/RR_Member_Search_NM.aspx?type=RRM&hkey=9450250f-beac-4459-ae9c-9ed5a13a9101#results"
htmlfile =urlopen(site)
soup = BeautifulSoup(htmlfile.read(), "html.parser")

table = soup.find_all('table')
# grab all values
rails = table[0].find_all("td")
    
i=0
while i < (len(rails)-1):
    name = rails[i].getText()
    website = rails[i+1].getText()
    print("Working on record: " + name + " " + website)
    
    #add to SQL Firmo DB
    cur.execute('''INSERT INTO US_Short_line_RR_II (name, website ) VALUES (?,?)''', (name,  website,))
    conn.commit()
    i=i+2





















