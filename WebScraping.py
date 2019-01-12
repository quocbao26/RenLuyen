import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
# %plt inline
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
# type(soup)

title = soup.title
print(title)
# text = soup.get_text()
# print(soup.text)
rows = soup.find_all('tr')
# print(rows[:10])
list_rows = []
for row in rows:
    cells = row.find_all('td')
    # print(row_td)
    str_cells = str(cells)
    # cleantext = BeautifulSoup(str_cells, 'lxml').get_text()
    # print(cleantext)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '', str_cells))
    list_rows.append(clean2)
print(list_rows)
df = pd.DataFrame(list_rows)
print(df.head(10))

df1 = df[0].str.split(',', expand=True)
print(df.head(10))
df1[0] = df1[0].str.strip('[')
df1.head(10)

col_labels = soup.find_all('th')
all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
all_header.append(cleantext2)
print(all_header)
df2 = pd.DataFrame(all_header)
df2.head()
df3 = df2[0].str.split(',', expand=True)
df3.head()
frames = [df3, df1]

df4 = pd.concat(frames)
df4.head(10)
df5 = df4.rename(columns=df4.iloc[0])
df5.head()
df5.info()

df6 = df5.dropna(axis=0, how='any')
df7 = df6.drop(df6.index[0])
df7.head()
df7.rename(columns={'[Place': 'Place'},inplace=True)
df7.rename(columns={' Team]': 'Team'},inplace=True)
df7.head()
df7['Team'] = df7['Team'].str.strip(']')
df7.head()