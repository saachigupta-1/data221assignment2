#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
from collections import Counter

input_text_filename = "sample-file.txt"

with open(input_text_filename, "r") as text_file:
    full_text_content = text_file.read()

raw_word_tokens = full_text_content.split()
cleaned_word_tokens = []

for single_token in raw_word_tokens:
    lowercase_token = single_token.lower()
    stripped_token = lowercase_token.strip(string.punctuation)

    alphabetic_character_count = sum(
        char.isalpha() for char in stripped_token
    )

    if alphabetic_character_count >= 2:
        cleaned_word_tokens.append(stripped_token)

word_frequency_counter = Counter(cleaned_word_tokens)

top_ten_words = word_frequency_counter.most_common(10)

for word, frequency in top_ten_words:
    print(f"{word} -> {frequency}")



# In[ ]:




