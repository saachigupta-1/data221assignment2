#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup

wikipedia_page_url = "https://en.wikipedia.org/wiki/Data_science"

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(wikipedia_page_url, headers=headers)

parsed_html_page = BeautifulSoup(response.text, "html.parser")


main_content_div = parsed_html_page.find("div", id="mw-content-text")

if main_content_div is None:
    print("Error: Could not find main content on the page.")
else:
    excluded_heading_keywords = ["references", "external links", "see also", "notes"]

    filtered_section_headings = []

    for heading_tag in main_content_div.find_all("h2"):
        heading_text = heading_tag.get_text().replace("[edit]", "").strip()

        if not any(keyword in heading_text.lower() for keyword in excluded_heading_keywords):
            filtered_section_headings.append(heading_text)

    with open("headings.txt", "w", encoding="utf-8") as output_file:
        for heading in filtered_section_headings:
            output_file.write(heading + "\n")

    print(f"Saved {len(filtered_section_headings)} headings to headings.txt")


# In[ ]:




