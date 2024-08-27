from textblob import TextBlob
import pandas as pd

def analyze_sentiment(headline):
    return TextBlob(headline).sentiment.polarity

def sentiment_analysis(df):
    df['Sentiment'] = df['headline'].apply(analyze_sentiment)
    return df
