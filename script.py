from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment

def extract_key_takeaways(text):
    # Tokenize the text
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    # Extract top keywords (you can customize this logic further)
    key_words = filtered_words[:5]  # Just taking the first 5 words as key takeaways
    return key_words

def main():
    # Take user input for the news article
    article = input("Please enter the news article: ")

    # Analyze sentiment
    sentiment = analyze_sentiment(article)
    print("\nSentiment Analysis:")
    print(f"Polarity: {sentiment.polarity}")
    print(f"Subjectivity: {sentiment.subjectivity}")

    # Extract key takeaways
    key_takeaways = extract_key_takeaways(article)
    print("\nKey Takeaways:")
    for i, takeaway in enumerate(key_takeaways, start=1):
        print(f"{i}. {takeaway}")

if __name__ == "__main__":
    main()
