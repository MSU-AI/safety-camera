import pandas as pd
from nltk.corpus import stopwords
from textblob import Word, TextBlob
stop_words=stopwords.words('english')
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def replace_non_alphanumeric(text):
    result = ""
    for char in text:
        if char.isalnum() or char.isspace():
            result += char
    return result

def preprocess_texts(text):
    processed_text = replace_non_alphanumeric(text)
    processed_text = " ".join(word for word in processed_text.split() if word not in stop_words)
    processed_text = " ".join(Word(word).lemmatize() for word in processed_text.split())
    return processed_text

def get_polarity_subjectivity(preprocess_text):
    processed_text=preprocess_texts(preprocess_text)
    polarity = TextBlob(processed_text).sentiment[0]
    subjectivity = TextBlob(processed_text).sentiment[1]
    return polarity, subjectivity

def sentiment_analysis(text):
    processed_text=preprocess_texts(text)
    sia=SentimentIntensityAnalyzer()
    sentiment=sia.polarity_scores(text)
    return sentiment

# use microphone input in the future.
text=input()

dict_sentiment = (sentiment_analysis(text))
score = dict_sentiment['compound']
if score < -.3:
    print("Alert")
