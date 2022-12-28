#### Module : testing (twitter)


## libraries
import data_loading
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
import sys


def model_20_testing(data, data2):
    
    #### feature engineering
    df = pd.DataFrame(data=data)
    X = df[['text', 
            'polarity_pos', 
            'polarity_neg', 
            'polarity_compound',
            'emotion_code']]
    vectorizer = TfidfVectorizer(max_features = 20000, ngram_range =(1,3), analyzer='char')
    column_transformer = ColumnTransformer(
        [('tfidf', vectorizer, 'text')],
        remainder='passthrough')
    X = column_transformer.fit_transform(X)
    y = df['class']
    
    #### train test data split
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 0)
    
    #### classifier
    clf = LinearSVC(dual=False, max_iter=1000)
    clf.fit(X_train, y_train)

    #### prediction
    data2["class"] =""
    for n in range(len(data2)):
        x = [[data2.text.iloc[n], data2.polarity_pos.iloc[n], data2.polarity_neg.iloc[n], data2.polarity_compound.iloc[n], data2.emotion_code.iloc[n]]]    
        x = pd.DataFrame(x)
        x.columns =['text', 'polarity_pos', 'polarity_neg', 'polarity_compound','emotion_code']
        vec = column_transformer.transform(x)
        data2['class'].iloc[n] = clf.predict(vec)
        if data2['class'].iloc[n] == "suicide":
            data2['class'].iloc[n] = 'suicide'
        elif data2['class'].iloc[n] == "non-suicide":
            data2['class'].iloc[n] = 'non-suicide'
        
    return data2

#### print result
# for n in range(len(data3)):
#     sys.stdout.buffer.write(str(n).encode("utf-8") + b'. ' + data3.ori_text.iloc[n].encode("utf-8") + b'\n')
#     print("pos: " + str(data3['polarity_pos'].iloc[n]) + " " +
#           "neg: " + str(data3['polarity_neg'].iloc[n] ) + " " +
#           "compound: " + str(data3['polarity_compound'].iloc[n]) + " " +
#           "emotion: " + str(data3['emotion'].iloc[n])
#           )
#     print("prediction class : " + data3['class'].iloc[n] + '\n')
