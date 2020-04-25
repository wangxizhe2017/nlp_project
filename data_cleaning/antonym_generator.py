#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[105]:


import nltk
from nltk.corpus import wordnet as wn


# In[2]:


import sys
sys.path.insert(0, '..')


# In[143]:


import csv


# In[27]:


f = open('train_sentence_5.txt', 'r')


# In[28]:


train_sentence_5 = list()


# In[29]:


for line in f:
    train_sentence_5.append(line)


# In[125]:


def get_antonyms(word):
    antonyms = []
    for syn in wn.synsets(word): 
        for l in syn.lemmas(): 
            if l.antonyms(): 
                antonyms.append(l.antonyms()[0].name())
    if len(antonyms) > 0:
        return antonyms[0]


# In[148]:


def antonym_generator_main(line):
    line = line.split('\t')
    left = line[0][2:-3].split("', '")
    right = line[1][2:-3].split("', '")
    zipped = zip(left, right)
    new_line = list()
    count = 0
    for word in zipped:
        if word[0] == "n't":
            left.pop(word[0])
            returned.append(left)
            break
        elif word[1] == 'ADJ' or word[1] == 'ADV' and get_antonyms(word[0]):
            count += 1
            if count % 2 == 1:
                new_line.append(get_antonyms(word[0]))
            else:
                new_line.append(word[0])
        elif word[1] == 'V':
            count += 1
            if count %2 == 1:
                new_line.append('not')
                new_line.append(word[0])
            else:
                new_line.append(word[0])
        else:
            new_line.append(word[0])
    return new_line


# In[145]:


# returned = list()
# for line in train_sentence_5:
#     line = line.split('\t')
#     left = line[0][2:-3].split("', '")
#     right = line[1][2:-3].split("', '")
#     zipped = zip(left, right)
#     new_line = list()
#     count = 0
#     for word in zipped:
#         if word[0] == "n't":
#             left.pop(word[0])
#             returned.append(left)
#             break
#         elif word[1] == 'ADJ' or word[1] == 'ADV' and get_antonyms(word[0]):
#             count += 1
#             if count % 2 == 1:
#                 new_line.append(get_antonyms(word[0]))
#             else:
#                 new_line.append(word[0])
#         elif word[1] == 'V':
#             count += 1
#             if count %2 == 1:
#                 new_line.append('not')
#                 new_line.append(word[0])
#             else:
#                 new_line.append(word[0])
#         else:
#             new_line.append(word[0])
#     returned.append(new_line)


# In[142]:


# print(returned[:5])


# In[146]:


# with open("antonym_sentences.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(returned)


# In[147]:


with open("file.txt", "w") as output:
    output.write(str(returned))


# In[ ]:




