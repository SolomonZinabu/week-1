import pandas as pd

from transformers import pipeline

def perform_sentiment_analysis(headlines):
    sentiment_analyzer = pipeline("sentiment-analysis")
    sentiments = sentiment_analyzer(headlines.tolist())
    return pd.DataFrame(sentiments)

# Example Usage:
# sentiments = perform_sentiment_analysis(analyst_data['headline'])
