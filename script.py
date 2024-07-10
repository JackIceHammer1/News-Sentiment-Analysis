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
    # Ask user how many pieces of text to analyze
    num_texts = int(input("How many pieces of text do you want to analyze? "))
    
    for i in range(num_texts):
        print(f"\nText {i + 1}:")
        text = input("Please enter the text to analyze: ")

        # Analyze sentiment
        sentiment = analyze_sentiment(text)
        print("\nSentiment Analysis:")
        print(f"Polarity: {sentiment.polarity}")
        print(f"Subjectivity: {sentiment.subjectivity}")

        # Extract key takeaways
        key_takeaways = extract_key_takeaways(text)
        print("\nKey Takeaways:")
        for j, takeaway in enumerate(key_takeaways, start=1):
            print(f"{j}. {takeaway}")

if __name__ == "__main__":
    main()
