#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
from collections import defaultdict

input_text_filename = "sample-file.txt"

def normalize_text_line(original_line):
    lowercase_line = original_line.lower()
    normalized_line = "".join(
        char for char in lowercase_line if char.isalnum()
    )
    return normalized_line

normalized_line_groups = defaultdict(list)

with open(input_text_filename, "r") as text_file:
    for line_number, original_line in enumerate(text_file, start=1):
        normalized_key = normalize_text_line(original_line)
        normalized_line_groups[normalized_key].append(
            (line_number, original_line.strip())
        )

near_duplicate_sets = [
    group for group in normalized_line_groups.values()
    if len(group) > 1
]

print("Number of near-duplicate sets:", len(near_duplicate_sets))

for duplicate_set in near_duplicate_sets[:2]:
    print("\nSet:")
    for line_number, original_text in duplicate_set:
        print(f"{line_number}: {original_text}")

