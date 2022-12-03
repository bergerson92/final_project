#https://github.com/learn-tech-trends/wikidata-api/blob/master/main.py solution do get wiki data via api
#https://github.com/alanjones2/Alan-Jones-article-code/blob/master/Wikitable/wikitable.ipynb good solution how to fetch data from wiki tables

import pandas as pd
#import matplotlib.pyplot as plt

url="https://en.wikipedia.org/wiki/List_of_world_records_in_Olympic_weightlifting"
#infotable = pd.read_html(url,match="record", flavor="bs4") kleines r weird output
#no outut for woman, only for men
#old output with men as input
#til row 38 men
#again new table til row 38 women
infotable = pd.read_html(url,match="Record", flavor="bs4")
print(infotable[0])
print(infotable[1])
