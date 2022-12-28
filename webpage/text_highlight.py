from nltk.sentiment.vader import SentimentIntensityAnalyzer
from termcolor import colored



def highlight_keyword (data):
    vader = SentimentIntensityAnalyzer()
    def testing(data):
        pos_word =[]
        neg_word =[]
        text = data.split()
        for n2 in range(len(text)):
            if vader.polarity_scores(text[n2])['pos'] != 0:
                    pos_word.append(text[n2])
            elif vader.polarity_scores(text[n2])['neg'] != 0:
                    neg_word.append(text[n2])
        return pos_word , neg_word
    
    pos, neg = testing(data)
    print(data)
    print(pos)
    print(neg)
    
    replaced_text = data
    for n in range(len(pos)):
        replaced_text = replaced_text.replace(pos[n], colored(pos[n], "green"))
        # replaced_text = replaced_text.replace(pos[n], "("+pos[n]+")")
    for n in range(len(neg)):
        replaced_text = replaced_text.replace(neg[n], colored(neg[n], "red"))
        # replaced_text = replaced_text.replace(neg[n], "["+neg[n]+"]")
    print('\n'+replaced_text)
    
    return replaced_text