from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def perform_topic_modeling(headlines, num_topics=5):
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    dtm = vectorizer.fit_transform(headlines)
    lda = LatentDirichletAllocation(n_components=num_topics)
    lda.fit(dtm)
    return lda, vectorizer

# Example Usage:
# lda_model, vectorizer = perform_topic_modeling(analyst_data['headline'])
