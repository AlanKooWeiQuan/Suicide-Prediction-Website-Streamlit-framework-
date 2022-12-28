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
    

# data = data_loading.load_data(r'C:\Users\AlanKoo99\Desktop\FYP coding\data\experiment_test_2_emotion.csv')
# text = 'I have no idea what i can do, maybe i should not live in this world. i need helpjust help me im crying so hard.'

# text = """I’m scared.   Everything just seems to be getting worse and worse. I’m young and I think I’m transgender but I’m not even sure about that. I can’t tell if I’m just lying to myself or if I’m actually trans, I feel so overwhelmed with thoughts and emotions and I can’t just take it anymore.
# I just wish I could at least know for sure if I was trans, and even then I have to worry about if my (religious) family will be accepting and if I can actually do anything to alleviate my pain a bit.
# I cut myself for the first time yesterday, I barely even drew blood so I can’t even fucking hurt myself correctly. I don’t think I’ll ever be able to do anything correctly, I want to pursue music but I know there’s no money to be found in that field unless I become famous but that’s not happening. 
# Currently I’m not seriously debating suicide but the thoughts keep coming back and they just keep getting worse. I’m not sure if I can really take this much longer, I just wish I was born a girl. I want to cry."""

# text = "I cannot stand it anymore! It is very pressure and stress until i not sleeping well every single night. I think i should end my life and release from this cruel world......"
#
# # text = input("Type something for suicide prediction: ")
# # print("Input Successful" + '\n')
# # model_20_testing(data, text)
#
# while (text != "exit"):  
#     text = input("\nType something for suicide prediction: ")
#     print("Input Successful" + '\n')
#     if(text == "exit"):  
#         break
#     model_20_testing(data, text) 
      
