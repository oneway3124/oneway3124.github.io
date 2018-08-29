import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


NUM_COLUMNS = 5
df = pd.read_csv("schedule.csv")
df =df.replace(np.NaN, "")
df_cols = df.columns[:NUM_COLUMNS]
html_table = df[df_cols].to_html()

with open('index.html','r') as f:
    s = f.read()
    
soup = BeautifulSoup(s,'html.parser')
soup.find("div", {"id": "schedule"}).string=""
soup.find("div", {"id": "schedule"}).append(BeautifulSoup(html_table, 'html.parser'))

with open('index.html','w') as f:
    f.write(str(soup.prettify()))