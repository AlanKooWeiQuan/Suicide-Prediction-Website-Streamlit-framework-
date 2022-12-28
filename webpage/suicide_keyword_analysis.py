#### Module : Suicide Keyword Analysis

## libraries
import data_loading
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from termcolor import colored
import streamlit as st


def suicide_keyword_analysis(data):
    

    ### remove non-suicide class
    word = data.columns[1]
    for n in range(len(data)):
        if (data.loc[n,word]) == "non-suicide":
            data = data.drop(n)
    data.reset_index(drop=True, inplace=True)
    
    ## return pos and neg words
    vader = SentimentIntensityAnalyzer()
    data["pos_word"] =""
    data["neg_word"] =""
    for n in range (len(data)):
        text = data.text.iloc[n]
        for n2 in range(len(text.split())):
            if vader.polarity_scores(text.split()[n2])['pos'] != 0:
                if data.pos_word.iloc[n] != None:
                    data.pos_word.iloc[n] += (" "+text.split()[n2])
                else:
                    data.pos_word.iloc[n] += (text.split()[n2])
            elif vader.polarity_scores(text.split()[n2])['neg'] != 0:
                if data.neg_word.iloc[n] != None:
                    data.neg_word.iloc[n] += (" "+text.split()[n2])
                else:
                    data.neg_word.iloc[n] += (text.split()[n2])
                     
    ### frequency count function
    def freq(data):
        pos_str2 =[]
        pos_str3 = []
        neg_str2 = []
        neg_str3 = []
        df_pos = pd.DataFrame()
        df_pos["word"]=''
        df_pos["frequency"]=''
        df_neg = pd.DataFrame()
        df_neg["word"]=''
        df_neg["frequency"]=''
        for n in range (len(data)):
            pos_str1 = str(data.pos_word.iloc[n]).split()
            neg_str1 = str(data.neg_word.iloc[n]).split()   

            for i in pos_str1:
                pos_str2.append(i)            
                if i not in pos_str3:
                    pos_str3.append(i)
            
            for i in neg_str1:
                neg_str2.append(i)            
                if i not in neg_str3:
                    neg_str3.append(i)
            
            if n == len(data)-1:
                for i in range(0, len(pos_str3)):
                    df_pos = df_pos.append({'word' : pos_str3[i]}, ignore_index = True)
                    df_pos["frequency"].iloc[i] = pos_str2.count(pos_str3[i])
                    
                for i in range(0, len(neg_str3)):
                    df_neg = df_neg.append({'word' : neg_str3[i]}, ignore_index = True)
                    df_neg["frequency"].iloc[i] = neg_str2.count(neg_str3[i])
        return df_pos, df_neg
    
    
    # ### word cloud function
    # def word_cloud(data):
    #     comment_words = ''
    #     # stopwords = set(STOPWORDS)
    #     stopwords = ""
    #
    #     for val in data:
    #         val = str(val)
    #         tokens = val.split()
    #         for i in range(len(tokens)):
    #             tokens[i] = tokens[i].lower()
    #         comment_words += " ".join(tokens)+" "
    #
    #     wordcloud = WordCloud(width = 3000, height = 2000,
    #                 background_color ='white',
    #                 stopwords = stopwords,
    #                 min_font_size = 10,
    #                 random_state= 6,
    #                 collocations = False,
    #                 prefer_horizontal = 1,
    #                 max_words = 200
    #                 ).generate(comment_words)
    #
    #     plt.figure(figsize = (8, 8), facecolor = None)
    #     plt.imshow(wordcloud)
    #     plt.axis("off")
    #     plt.tight_layout(pad = 0)
    #     plt.show()
    #     st.pyplot(plt)
    
    ### Seperation of Data
    # sentiment polarity class
    neg_class = data[data['sentiment polarity class'] == 'negative']
    neg_class.reset_index(drop=True, inplace=True)
    pos_class = data[data['sentiment polarity class'] == 'positive']
    pos_class.reset_index(drop=True, inplace=True)
    neutral_class = data[data['sentiment polarity class'] == 'neutral']
    neutral_class.reset_index(drop=True, inplace=True)    
    
    # sentiment polarity level
    vry_strong_pos = data[data['sentiment polarity level'] == 'very strong positive']
    vry_strong_pos.reset_index(drop=True, inplace=True)
    strong_pos = data[data['sentiment polarity level'] == 'strong positive']
    strong_pos.reset_index(drop=True, inplace=True)
    medium_pos = data[data['sentiment polarity level'] == 'medium positive']
    medium_pos.reset_index(drop=True, inplace=True)
    weak_pos = data[data['sentiment polarity level'] == 'weak positive']
    weak_pos.reset_index(drop=True, inplace=True)
    vry_weak_pos = data[data['sentiment polarity level'] == 'very weak positive']
    vry_weak_pos.reset_index(drop=True, inplace=True)
    vry_strong_neg = data[data['sentiment polarity level'] == 'very strong negative']
    vry_strong_neg.reset_index(drop=True, inplace=True)
    strong_neg = data[data['sentiment polarity level'] == 'strong negative']
    strong_neg.reset_index(drop=True, inplace=True)
    medium_neg = data[data['sentiment polarity level'] == 'medium negative']
    medium_neg.reset_index(drop=True, inplace=True)
    weak_neg = data[data['sentiment polarity level'] == 'weak negative']
    weak_neg.reset_index(drop=True, inplace=True)
    vry_weak_neg = data[data['sentiment polarity level'] == 'very weak negative']
    vry_weak_neg.reset_index(drop=True, inplace=True)
    
    #emotion
    negative_emt = data[data['emotion'] == 'negative']
    negative_emt.reset_index(drop=True, inplace=True)
    positive_emt = data[data['emotion'] == 'positive']
    positive_emt.reset_index(drop=True, inplace=True)
    fear_emt = data[data['emotion'] == 'fear']
    fear_emt.reset_index(drop=True, inplace=True)
    trust_emt = data[data['emotion'] == 'trust']
    trust_emt.reset_index(drop=True, inplace=True)
    anticipation_emt = data[data['emotion'] == 'anticipation']
    anticipation_emt.reset_index(drop=True, inplace=True)
    anger_emt = data[data['emotion'] == 'anger']
    anger_emt.reset_index(drop=True, inplace=True)
    surprise_emt = data[data['emotion'] == 'surprise']
    surprise_emt.reset_index(drop=True, inplace=True)
    sadness_emt = data[data['emotion'] == 'sadness']
    sadness_emt.reset_index(drop=True, inplace=True)
    joy_emt = data[data['emotion'] == 'joy']
    joy_emt.reset_index(drop=True, inplace=True)
    disgust_emt = data[data['emotion'] == 'disgust']
    disgust_emt.reset_index(drop=True, inplace=True)
    
    
    ### Print Frequency Data and Word Cloud
    ## whole data 
    # data_pos, data_neg = freq(data)
    # word_cloud(data.pos_word)
    # print(data_neg)
    # data_neg.to_csv(r'C:\Users\AlanKoo99\Desktop\data_neg.csv', index = False)
    # word_cloud(data.neg_word)
    #
    # ## sentiment polarity class
    # # neg class
    # neg_class_data_pos, neg_class_data_neg = freq(neg_class)
    # word_cloud(neg_class.pos_word)
    # word_cloud(neg_class.neg_word)
    # # pos class
    # pos_class_data_pos, pos_class_data_neg = freq(pos_class)
    # word_cloud(pos_class.pos_word)
    # word_cloud(pos_class.neg_word)
    # # neutral class
    # neutral_class_data_pos, neutral_class_data_neg = freq(neutral_class)
    # word_cloud(neutral_class.pos_word)
    # word_cloud(neutral_class.neg_word)
    #
    # ## sentiment polarity level
    # # very strong positive
    # vry_strong_pos_data_pos, vry_strong_pos_data_neg = freq(vry_strong_pos)
    # word_cloud(vry_strong_pos.pos_word)
    # word_cloud(vry_strong_pos.neg_word)
    # # strong positive
    # strong_pos_data_pos, strong_pos_data_neg = freq(strong_pos)
    # word_cloud(strong_pos.pos_word)
    # word_cloud(strong_pos.neg_word)
    # # medium positive
    # medium_pos_data_pos, medium_pos_data_neg = freq(medium_pos)
    # word_cloud(medium_pos.pos_word)
    # word_cloud(medium_pos.neg_word)
    # # weak positive
    # weak_pos_data_pos, weak_pos_data_neg = freq(weak_pos)
    # word_cloud(weak_pos.pos_word)
    # word_cloud(weak_pos.neg_word)
    # # very weak positive
    # vry_weak_pos_data_pos, vry_weak_pos_data_neg = freq(vry_weak_pos)
    # word_cloud(vry_weak_pos.pos_word)
    # word_cloud(vry_weak_pos.neg_word)
    # # very strong negative
    # vry_strong_neg_data_pos, vry_strong_neg_data_neg = freq(vry_strong_neg)
    # word_cloud(vry_strong_neg.pos_word)
    # word_cloud(vry_strong_neg.neg_word)
    # # strong negative
    # strong_neg_data_pos, strong_neg_data_neg = freq(strong_neg)
    # word_cloud(strong_neg.pos_word)
    # word_cloud(strong_neg.neg_word)
    # # medium negative
    # medium_neg_data_pos, medium_neg_data_neg = freq(medium_neg)
    # word_cloud(medium_neg.pos_word)
    # word_cloud(medium_neg.neg_word)
    # # weak negative
    # weak_neg_data_pos, weak_neg_data_neg = freq(weak_neg)
    # word_cloud(weak_neg.pos_word)
    # word_cloud(weak_neg.neg_word)
    # # very weak negative
    # vry_weak_neg_data_pos, vry_weak_neg_data_neg = freq(vry_weak_neg)
    # word_cloud(vry_weak_neg.pos_word)
    # word_cloud(vry_weak_neg.neg_word)
    #
    # ## emotion
    # # negative
    # negative_emt_data_pos, negative_emt_data_neg = freq(negative_emt)
    # word_cloud(negative_emt.pos_word)
    # word_cloud(negative_emt.neg_word)
    # positive
    # positive_emt_data_pos, positive_emt_data_neg = freq(positive_emt)
    # word_cloud(positive_emt.pos_word)
    # word_cloud(positive_emt.neg_word)
    # # fear
    # fear_emt_data_pos, fear_emt_data_neg = freq(fear_emt)
    # word_cloud(fear_emt.pos_word)
    # word_cloud(fear_emt.neg_word)
    # # trust
    # trust_emt_data_pos, trust_emt_data_neg = freq(trust_emt)
    # word_cloud(trust_emt.pos_word)
    # word_cloud(trust_emt.neg_word)
    # # anticipation
    # anticipation_emt_data_pos, anticipation_emt_data_neg = freq(anticipation_emt)
    # word_cloud(anticipation_emt.pos_word)
    # word_cloud(anticipation_emt.neg_word)
    # # anger
    # anger_emt_data_pos, anger_emt_data_neg = freq(anger_emt)
    # word_cloud(anger_emt.pos_word)
    # word_cloud(anger_emt.neg_word)
    # # surprise
    # surprise_emt_data_pos, surprise_emt_data_neg = freq(surprise_emt)
    # word_cloud(surprise_emt.pos_word)
    # word_cloud(surprise_emt.neg_word)
    # # sadness
    # sadness_emt_data_pos, sadness_emt_data_neg = freq(sadness_emt)
    # word_cloud(sadness_emt.pos_word)
    # word_cloud(sadness_emt.neg_word)
    # # joy
    # joy_emt_data_pos, joy_emt_data_neg = freq(joy_emt)
    # word_cloud(joy_emt.pos_word)
    # word_cloud(joy_emt.neg_word)
    # # disgust
    # disgust_emt_data_pos, disgust_emt_data_neg = freq(disgust_emt)
    # word_cloud(disgust_emt.pos_word)
    # word_cloud(disgust_emt.neg_word) 

    
    return data


### word cloud function
def word_cloud(data):
    comment_words = ''
    # stopwords = set(STOPWORDS)
    stopwords = ""
    
    for val in data:
        val = str(val)
        tokens = val.split()
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()
        comment_words += " ".join(tokens)+" "
    
    wordcloud = WordCloud(width = 3000, height = 2000,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10,
                random_state= 6,
                collocations = False,
                prefer_horizontal = 1,
                max_words = 200
                ).generate(comment_words)
    
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()
    st.pyplot(plt)