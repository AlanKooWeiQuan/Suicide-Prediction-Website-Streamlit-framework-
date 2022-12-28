#### Module : Data Preprocessing

## libraries
import string
import nltk
from nltk.tokenize import word_tokenize
import contractions
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re

## 1) row removal of missing data
def  row_removal_missing_data(data):
    data = data.dropna()
    data.reset_index(drop=True, inplace=True)
    return data


## 2) row removal of unwanted class
def row_removal_of_unwated_class(data):
    word = data.columns[1]
    for n in range(len(data)):
        if (data.loc[n,word]) != "suicide" and (data.loc[n,word]) != "non-suicide":
            data = data.drop(n)
    data.reset_index(drop=True, inplace=True)
    return data        


## 3) contraction expansion
def expand_contractions(data):
    word = data.columns[0]
    for n in range(len(data)) :
        data.loc[n,word] = " ".join([contractions.fix(word) for word in data.loc[n,word].split()])
    return data


## 4) punctuation removal
def punctuation_removal(data):
    word = data.columns[0]
    for n in range(len(data)) :
        data.loc[n,word] = "".join([i for i in data.loc[n,word] if i not in string.punctuation])
    return data
    
    
## 5) stop words removal
stopwords = nltk.corpus.stopwords.words('english')
def stop_words_removal (data):
    word = data.columns[0]
    for n in range(len(data)) :
        data.loc[n,word] = word_tokenize(data.loc[n,word])
        data.loc[n,word]= " ".join([i for i in data.loc[n,word] if i not in stopwords])
    return data
    
   
## 6) lower casing
def lower_casing (data):
    word = data.columns[0]
    data[word] = data[word].str.lower()
    return data


## 7) stemming
stemmer = PorterStemmer()
def stemming(data):
    word = data.columns[0]
    for n in range(len(data)) :
        data.loc[n,word] = word_tokenize(data.loc[n,word])
        data.loc[n,word] = " ".join([stemmer.stem(word) for word in data.loc[n,word]])
    return data

## 8) lemmatization
lemmatizer = WordNetLemmatizer()
def lemmatization(data):
    word = data.columns[0]
    for n in range(len(data)) :
        data.loc[n,word] = word_tokenize(data.loc[n,word])
        data.loc[n,word] = " ".join([lemmatizer.lemmatize (word, pos ='v') for word in data.loc[n,word]])
    return data

## 9) Digit removal
def digit_removal (data):
    word = data.columns[0]
    for n in range(len(data)) :
        data.loc[n,word] = word_tokenize(data.loc[n,word])
        data.loc[n,word]= " ".join([i for i in data.loc[n,word] if i.isalpha()])
    return data


## 10) removal or rephrase of unnecessary pattern of text
def removal_rephrase_unwanted_pattern_text(data):
    word = data.columns[0]
    for n in range(len(data)) : 
        data.loc[n,word] = re.sub('\n','',data.loc[n,word]) # \n
        data.loc[n,word] = re.sub('\s+',' ',data.loc[n,word]) #double spacing
        data.loc[n,word] = re.sub('\A[ ]','',data.loc[n,word]) # a empty space at start of sentence   
    return data

## 11) removal of duplicate data
def removal_duplicate_data(data):
    data = data.drop_duplicates(keep=False)
    data.reset_index(drop=True, inplace=True)
    return data








