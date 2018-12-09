# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import json
import sys
from pandas import Series, DataFrame
with open("jsondb.txt",encoding="utf-8") as f:
        line=f.readline()
        result=json.loads(line)
#         print(result) 
        siblings = DataFrame(result['subjects'])
        print(siblings.columns)
        print(siblings.sort_values("rate"))
        
 #######################################################################
 import requests
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=rank&page_limit=100&page_start=0'
resp = requests.get(url)
resp.text
data=json.loads(resp.text)
issue_labels = DataFrame(data["subjects"])
issue_labels
        
