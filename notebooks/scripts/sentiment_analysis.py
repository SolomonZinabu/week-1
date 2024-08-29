import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon')

def perform_sentiment_analysis(headlines):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []
    for headline in headlines:
        sentiment_score = analyzer.polarity_scores(headline)
        sentiments.append({
            'headline': headline,
            'sentiment': sentiment_score['compound'],  # Overall sentiment score
            'positive': sentiment_score['pos'],
            'neutral': sentiment_score['neu'],
            'negative': sentiment_score['neg']
        })
    return pd.DataFrame(sentiments)
