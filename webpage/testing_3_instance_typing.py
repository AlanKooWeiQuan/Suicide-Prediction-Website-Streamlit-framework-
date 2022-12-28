#### Module : testing (instance typing)


## libraries
# import data_loading
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nrclex import NRCLex

def model_20_testing(data, text):
    
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
    vader = SentimentIntensityAnalyzer()
    emotion = NRCLex(text)
    if emotion.top_emotions[0][0] == "fear" :
        emotion_code = 1
    elif emotion.top_emotions[0][0] == "anger":
        emotion_code = 2
    elif emotion.top_emotions[0][0] == "anticipation" :
        emotion_code = 3
    elif emotion.top_emotions[0][0] == "trust":
        emotion_code = 4
    elif emotion.top_emotions[0][0] == "surprise":
        emotion_code = 5
    elif emotion.top_emotions[0][0] == "positive" :
        emotion_code = 6
    elif emotion.top_emotions[0][0] == "negative":
        emotion_code = 7
    elif emotion.top_emotions[0][0] == "sadness":
        emotion_code = 8
    elif emotion.top_emotions[0][0] == "disgust" :
        emotion_code = 9
    elif emotion.top_emotions[0][0] == "joy":
        emotion_code = 10
        
    x = [[text, vader.polarity_scores(text)['pos'], vader.polarity_scores(text)['neg'], (vader.polarity_scores(text)['compound']+1), emotion_code]]    
    x = pd.DataFrame(x)
    x.columns =['text', 'polarity_pos', 'polarity_neg', 'polarity_compound','emotion_code']
    print("text input : \n" + text)
    # print(x)
    print("pos: " + str(x['polarity_pos'].iloc[0]) + " " +
          "neg: " + str(x['polarity_neg'].iloc[0] ) + " " +
          "compound: " + str(x['polarity_compound'].iloc[0]) + " " +
          "emotion: " + str(emotion.top_emotions[0][0])
          )
    vec = column_transformer.transform(x)
    print("prediction class : " + clf.predict(vec))
    
    return str(round(x['polarity_pos'].iloc[0],3)), str(round(x['polarity_neg'].iloc[0],3)), "compound: " + str(round(x['polarity_compound'].iloc[0],3)), str(emotion.top_emotions[0][0]), clf.predict(vec)
    
