# Sentiment Analysis with TextBlob

## Overview

This project implements a basic sentiment analysis tool using TextBlob to analyze sample text data and classify sentiments as Positive, Negative, or Neutral.

## Requirements

- Python 3.x
- textblob
- pandas

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Install dependencies:

   ```bash
   pip install textblob pandas
   ```

3. Download TextBlob corpora (run once):

   ```bash
   python -m textblob.download_corpora
   ```

## Usage

1. Run the script:

   ```bash
   python Sentiment_Analysis.py
   ```

2. The script outputs a table of results and saves them to `sentiment_results.csv`.

## Project Structure

- `Sentiment_Analysis.py`: Main script containing the sentiment analysis implementation
- `README.md`: Project documentation
- `sentiment_results.csv`: Output file with text, polarity, and sentiment

## Notes

- The script uses a small sample dataset of text reviews.
- Polarity ranges from -1 (negative) to 1 (positive), with 0 as neutral.
- Results are saved as a CSV file for further analysis.