#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/Machine_learning"


headers = {"User-Agent": "Mozilla/5.0"}


response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


content = soup.find("div", id="mw-content-text")

if content is None:
    print("Error: Could not find main content on the page.")
else:
    tables = content.find_all("table")

    if not tables:
        print("No tables found in the page.")
    else:
        table = None
        for t in tables:
            rows = t.find_all("tr")
            if len(rows) >= 4:
                table = t
                break

        if table is None:
            print("No table with at least 4 rows found.")
        else:
            rows = table.find_all("tr")
            headers = [th.get_text(strip=True) for th in rows[0].find_all("th")]

            data = []
            for row in rows[1:]:
                cols = [td.get_text(strip=True) for td in row.find_all(["td", "th"])]
                while len(cols) < len(headers):
                    cols.append("")
                data.append(cols)

            if not headers and data:
                headers = [f"col{i+1}" for i in range(len(data[0]))]

            df = pd.DataFrame(data, columns=headers)
            df.to_csv("wiki_table.csv", index=False)
            print(f"Saved table to wiki_table.csv with {len(df)} rows.")


# In[ ]:




