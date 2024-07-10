# News Analysis with Sentiment and Keyword Extraction

This Python script analyzes news articles or texts provided by the user. It performs sentiment analysis using TextBlob, extracts key emotional and financial impact words, identifies mentioned stock tickers, and summarizes the article. The analysis results are then displayed with descriptive ratings.

## Features

- **Sentiment Analysis**: Provides polarity and subjectivity scores rounded to four decimal places along with descriptive ratings (e.g., Positive, Highly subjective).
- **Key Emotional and Financial Impact Words**: Extracts relevant words related to emotions and financial impacts from the text.
- **Mentioned Stock Tickers**: Identifies stock tickers (e.g., AMD, NVDA) mentioned in the text.
- **Article Summary**: Summarizes the input article or text to provide a brief overview.
- **Input Handling**: Accepts multiple paragraphs of text input until terminated by `/./`.

## Usage

Follow the instructions to input the text and terminate input with /./.

## Requirements

- **Python 3.x**
  - The script is compatible with Python 3.x versions.
  
- **Dependencies**
  - Install required libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```
  - The following Python packages are required:
    - `textblob`: For sentiment analysis.
    - `nltk`: For tokenization and stopwords.
    - `gensim`: For keyword extraction. (NOTE: May require up to date Microsoft C++ Build Tools)
    - `scipy`: For scientific computing (used indirectly by `gensim`).

- **Operating System**
  - The script should work on any operating system that supports Python 3.x.
  
- **Input Format**
  - Input should be in plain text format. Multiple paragraphs are supported, terminated by `/./`.


