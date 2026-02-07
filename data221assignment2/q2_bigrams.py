#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
from collections import Counter

filename = "sample-file.txt"
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

    if sum(char.isalpha() for char in stripped_token) >= 2:
        cleaned_word_tokens.append(stripped_token)

bigram_list = []

for index in range(len(cleaned_word_tokens) - 1):
    first_word = cleaned_word_tokens[index]
    second_word = cleaned_word_tokens[index + 1]
    bigram_list.append(first_word + " " + second_word)

bigram_frequency_counter = Counter(bigram_list)

top_five_bigrams = bigram_frequency_counter.most_common(5)

for bigram, frequency in top_five_bigrams:
    print(f"{bigram} -> {frequency}")

