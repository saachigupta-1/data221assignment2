#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

headers = {
    "User-Agent": "Mozilla/5.0"
}


response = requests.get(url, headers=headers)


soup = BeautifulSoup(response.text, "html.parser")


if soup.title is not None:
    print("Title:", soup.title.text)
else:
    print("Title not found")

content_div = soup.find("div", id="mw-content-text")

if content_div is not None:
    for p in content_div.find_all("p"):
        text = p.get_text(strip=True)
        if len(text) >= 50:
            print("\nFirst paragraph:")
            print(text)
            break
else:
    print("Main content not found")


# In[ ]:




