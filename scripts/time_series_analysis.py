def analyze_publication_frequency(data):
    data['publication_date'] = pd.to_datetime(data['data'])
    return data.groupby(data['publication_date'].dt.date).size()

# Example Usage:
# publication_freq = analyze_publication_frequency(analyst_data)
