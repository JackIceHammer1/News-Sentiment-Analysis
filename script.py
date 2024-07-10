from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment

def get_sentiment_rating(polarity, subjectivity):
    # Assign descriptive ratings based on polarity
    if polarity < -0.5:
        polarity_rating = "Extremely negative"
    elif polarity < 0:
        polarity_rating = "Negative"
    elif polarity == 0:
        polarity_rating = "Neutral"
    elif polarity > 0.5:
        polarity_rating = "Extremely positive"
    else:
        polarity_rating = "Positive"
    
    # Assign descriptive ratings based on subjectivity
    if subjectivity < 0.2:
        subjectivity_rating = "Highly objective"
    elif subjectivity < 0.5:
        subjectivity_rating = "Slightly objective"
    elif subjectivity == 0.5:
        subjectivity_rating = "Neutral"
    elif subjectivity < 0.8:
        subjectivity_rating = "Slightly subjective"
    else:
        subjectivity_rating = "Highly subjective"
    
    return polarity_rating, subjectivity_rating

def extract_key_takeaways_and_tickers(text):
    # Tokenize the text
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word.lower() not in stop_words]

    # Expanded sets for emotional and financial impact words
    emotional_words = {
        'happy', 'sad', 'excited', 'anxious', 'fear', 'optimistic', 'pessimistic', 'confident', 'worried',
        'thrilled', 'disappointed', 'enthusiastic', 'concerned', 'hopeful', 'frustrated', 'angry', 'joyful',
        'surprised', 'shocked', 'elated', 'depressed', 'relieved', 'tense', 'content'
    }
    financial_words = {
        'profit', 'loss', 'revenue', 'investment', 'market', 'growth', 'decline', 'earnings', 'forecast',
        'sale', 'purchase', 'expense', 'income', 'debt', 'equity', 'capital', 'dividend', 'merger', 'acquisition',
        'valuation', 'cost', 'price', 'trend', 'cash', 'assets', 'liabilities', 'return', 'gain', 'drop',
        'rise', 'fall', 'increase', 'decrease', 'boost', 'cut', 'interest', 'inflation', 'deflation'
    }

    # Initialize sets to store unique key words and stock tickers
    key_words = set()
    stock_tickers = set()

    # Regex patterns to match stock ticker symbols
    ticker_pattern = re.compile(r'\b[A-Z]{3,4}\b')
    encased_ticker_pattern = re.compile(r'\((\b[A-Z]{3,4}\b)\)')

    # Iterate through filtered words and add relevant ones to key_words set
    for word in filtered_words:
        if word.lower() in emotional_words or any(financial_word in word.lower() for financial_word in financial_words):
            key_words.add(word)
    
    # Check if the word matches the ticker pattern
    for word in words:
        if ticker_pattern.match(word):
            stock_tickers.add(word)
        match = encased_ticker_pattern.match(word)
        if match:
            stock_tickers.add(match.group(1))

    # Convert sets to lists and return the first 5 unique key words and all stock tickers
    return list(key_words)[:5], list(stock_tickers)

def summarize_article(text):
    blob = TextBlob(text)
    sentences = blob.sentences
    if len(sentences) > 1:
        return str(sentences[0]) + " " + str(sentences[1])
    else:
        return str(sentences[0])

def main():
    # Ask user for the text to analyze
    print("Please enter the text to analyze (end input with /./ on a new line):")

    # Read multiple lines of input until the user types /./
    lines = []
    while True:
        line = input()
        if line == '/./':
            break
        lines.append(line)

    text = '\n'.join(lines)

    # Analyze sentiment
    sentiment = analyze_sentiment(text)
    polarity_rating, subjectivity_rating = get_sentiment_rating(sentiment.polarity, sentiment.subjectivity)

    # Round polarity and subjectivity to four decimal places
    rounded_polarity = round(sentiment.polarity, 4)
    rounded_subjectivity = round(sentiment.subjectivity, 4)

    print("\nSentiment Analysis:")
    print(f"Polarity: {rounded_polarity} ({polarity_rating})")
    print(f"Subjectivity: {rounded_subjectivity} ({subjectivity_rating})")

    # Extract key takeaways and stock tickers
    key_takeaways, stock_tickers = extract_key_takeaways_and_tickers(text)
    
    print("\nKey Emotional and Financial Impact Words:")
    if key_takeaways:
        for j, takeaway in enumerate(key_takeaways, start=1):
            print(f"{j}. {takeaway}")
    else:
        print("No relevant emotional or financial impact words found.")

    print("\nMentioned Stock Tickers:")
    if stock_tickers:
        for ticker in stock_tickers:
            print(f"- {ticker}")
    else:
        print("No stock tickers found.")

    # Summarize the article
    summary = summarize_article(text)
    print("\nArticle Summary:")
    print(summary)

if __name__ == "__main__":
    main()
