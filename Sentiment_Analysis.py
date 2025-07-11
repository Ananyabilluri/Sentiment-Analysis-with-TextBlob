# Sentiment Analysis with TextBlob
# A basic sentiment analysis implementation using TextBlob on sample text data

from textblob import TextBlob
import pandas as pd

# Sample text data
texts = [
    "I love this product, it's amazing!",
    "This is terrible, worst experience ever.",
    "The service was okay, nothing special.",
    "Absolutely fantastic, highly recommend!",
    "Not impressed, very disappointing."
]

# Perform sentiment analysis
results = []
for text in texts:
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    sentiment = 'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'
    results.append({'Text': text, 'Polarity': polarity, 'Sentiment': sentiment})

# Save results to CSV
df = pd.DataFrame(results)
df.to_csv('sentiment_results.csv', index=False)

print(df)