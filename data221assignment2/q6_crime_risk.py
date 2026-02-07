#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

crime_dataframe = pd.read_csv("crime.csv")

crime_dataframe["risk"] = crime_dataframe["ViolentCrimesPerPop"].apply(
    lambda crime_rate: "HighCrime" if crime_rate >= 0.50 else "LowCrime"
)

average_unemployment_by_risk = (
    crime_dataframe.groupby("risk")["PctUnemployed"].mean()
)

for risk_level, average_unemployment in average_unemployment_by_risk.items():
    print(
        f"{risk_level}: Average unemployment = {average_unemployment:.2f}"
    )


# In[ ]:




