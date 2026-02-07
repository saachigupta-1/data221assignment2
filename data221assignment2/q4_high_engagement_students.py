#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

student_dataframe = pd.read_csv("student.csv")

high_engagement_students = student_dataframe[
    (student_dataframe["studytime"] >= 3) &
    (student_dataframe["internet"] == 1) &
    (student_dataframe["absences"] <= 5)
]

high_engagement_students.to_csv(
    "high_engagement.csv", index=False
)

number_of_students_saved = len(high_engagement_students)
average_student_grade = high_engagement_students["grade"].mean()

print("Number of students:", number_of_students_saved)
print("Average grade:", average_student_grade)

