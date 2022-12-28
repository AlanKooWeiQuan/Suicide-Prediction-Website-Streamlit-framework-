#### Module : feature engineering (Emotion)


## libraries
from nrclex import NRCLex


def feature_engineering_Emotion(data):
    data["emotion"] =""
    data["emotion_code"] = ""
    for n in range(len(data)):
        emotion = NRCLex(data.text.iloc[n])
        data.emotion.iloc[n] = emotion.top_emotions[0][0]
        
        if emotion.top_emotions[0][0] == "fear" :
            data.emotion_code.iloc[n] = 1
        elif emotion.top_emotions[0][0] == "anger":
            data.emotion_code.iloc[n] = 2
        elif emotion.top_emotions[0][0] == "anticipation" :
            data.emotion_code.iloc[n] = 3
        elif emotion.top_emotions[0][0] == "trust":
            data.emotion_code.iloc[n] = 4
        elif emotion.top_emotions[0][0] == "surprise":
            data.emotion_code.iloc[n] = 5
        elif emotion.top_emotions[0][0] == "positive" :
            data.emotion_code.iloc[n] = 6
        elif emotion.top_emotions[0][0] == "negative":
            data.emotion_code.iloc[n] = 7
        elif emotion.top_emotions[0][0] == "sadness":
            data.emotion_code.iloc[n] = 8
        elif emotion.top_emotions[0][0] == "disgust" :
            data.emotion_code.iloc[n] = 9
        elif emotion.top_emotions[0][0] == "joy":
            data.emotion_code.iloc[n] = 10
        n = 0
        print(n)
        n +=1
    return data
