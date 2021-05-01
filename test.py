"""
  @file test.py
  @author Ken Jonathan Pais (SF ID:257137)
  @brief
  @version 1.0
  @date 2021-05-01
  @copyright Copyright (c) 2021
"""


#Importing requirements 

import pandas as pd
import re                                           
pd.set_option('display.max_colwidth', 200)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity         #using cosine similiarity algorithm for matching questions

#Setting up conversational Training Data

df = pd.read_csv('C:/Users/Admin/Desktop/L&T/STEPIn/MiniProjectPython/data.csv')
convo = df.iloc[:, 0]

#Matching Question-Answer pairs into a list

clist = []

def qa_pairs(x):
    cpairs = re.findall(": (.*?)(?:$|\n)", x)          #regular expression
    clist.extend(list(zip(cpairs, cpairs[1:])))
convo.map(qa_pairs);
convo_frame = pd.Series(dict(clist)).to_frame().reset_index()
convo_frame.columns = ['q', 'a']

#Matching closest question to user_input 

vectorizer = TfidfVectorizer(ngram_range=(1,3))
vec = vectorizer.fit_transform(convo_frame['q'])

def get_response(q):
    my_q = vectorizer.transform([q])
    cs = cosine_similarity(my_q, vec)
    rs = pd.Series(cs[0]).sort_values(ascending=False)
    rsi = rs.index[0]
    return convo_frame.iloc[rsi]['a']



if __name__ == '__main__':
    print('Talk with me')
    while True:
        p = str(input())
        print(get_response(p))
