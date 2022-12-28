#### Module : feature engineering (Sentiment Polarity)


## libraries
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def feature_engineering_Sentiment_Polarity (data):
    vader = SentimentIntensityAnalyzer()
    data["polarity_pos"] =""
    data["polarity_neg"] =""
    data["polarity_compound"] =""
    for n in range(len(data)):
        data.polarity_pos.iloc[n] = vader.polarity_scores(data.text.iloc[n])['pos']
        data.polarity_neg.iloc[n] = vader.polarity_scores(data.text.iloc[n])['neg']
        data.polarity_compound.iloc[n] = (vader.polarity_scores(data.text.iloc[n])['compound']+1)
        n = 0
        print(n)
        n +=1
    return data