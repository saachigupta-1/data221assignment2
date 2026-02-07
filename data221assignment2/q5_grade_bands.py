#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

student_dataframe = pd.read_csv("student.csv")

def assign_grade_band(final_grade):
    if final_grade <= 9:
        return "Low"
    elif final_grade <= 14:
        return "Medium"
    else:
        return "High"

student_dataframe["grade_band"] = (
    student_dataframe["grade"].apply(assign_grade_band)
)

grade_band_summary_table = student_dataframe.groupby("grade_band").agg(
    number_of_students=("grade", "count"),
    average_absences=("absences", "mean"),
    internet_access_percentage=("internet", "mean")
)

grade_band_summary_table["internet_access_percentage"] *= 100

grade_band_summary_table.to_csv("student_bands.csv")

print(grade_band_summary_table)


# In[ ]:




