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

def extract_key_takeaways(text):
    # Tokenize the text
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word.lower() not in stop_words]

    # Define sets for emotional and financial impact words
    emotional_words = {'happy', 'sad', 'excited', 'anxious', 'fear'}
    financial_words = {'profit', 'loss', 'revenue', 'investment', 'market'}

    # Initialize a set to store unique key words
    key_words = set()

    # Regex pattern to match stock ticker symbols (3 or 4 uppercase letters)
    ticker_pattern = re.compile(r'\b[A-Z]{3,4}\b')

    # Iterate through filtered words and add relevant ones to key_words set
    for word in filtered_words:
        if word.lower() in emotional_words or any(financial_word in word.lower() for financial_word in financial_words):
            key_words.add(word)
        
        # Check if the word matches the ticker pattern
        if ticker_pattern.match(word):
            key_words.add(word)

    # Convert set to list and return the first 5 unique words
    return list(key_words)[:5]

def summarize_article(text):
    blob = TextBlob(text)
    sentences = blob.sentences
    if len(sentences) > 1:
        return str(sentences[0]) + " " + str(sentences[1])
    else:
        return str(sentences[0])

def main():
    # Ask user for the text to analyze
    print("Please enter the text to analyze (paste multiple paragraphs):")
    text = input()

    # Analyze sentiment
    sentiment = analyze_sentiment(text)
    polarity_rating, subjectivity_rating = get_sentiment_rating(sentiment.polarity, sentiment.subjectivity)

    print("\nSentiment Analysis:")
    print(f"Polarity: {sentiment.polarity} ({polarity_rating})")
    print(f"Subjectivity: {sentiment.subjectivity} ({subjectivity_rating})")

    # Extract key takeaways
    key_takeaways = extract_key_takeaways(text)
    print("\nKey Emotional and Financial Impact Words including Stock Tickers:")
    if key_takeaways:
        for j, takeaway in enumerate(key_takeaways, start=1):
            print(f"{j}. {takeaway}")
    else:
        print("No relevant emotional or financial impact words found.")

    # Summarize the article
    summary = summarize_article(text)
    print("\nArticle Summary:")
    print(summary)

if __name__ == "__main__":
    main()
