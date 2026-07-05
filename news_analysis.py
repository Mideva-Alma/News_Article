import re
from news_article import news_article
from collections import Counter


# Count a specific word

def count_specific_word(text, search_word):
    words = re.findall(r'\b\w+\b', text.lower())
    count = 0

    for word in words:
        if word == search_word.lower():
            count += 1

    return count

# Identify the most common word

def identify_most_common_word(text):
    words = re.findall(r'\b\w+\b', text.lower())

    if not words:
        return ""

    word_counts = Counter(words)
    return word_counts.most_common(1)[0][0]

#Calculate average word length

def calculate_average_word_length(text):
    words = re.findall(r'\b\w+\b', text)

    if len(words) == 0:
        return 0.0

    total_length = 0

    for word in words:
        total_length += len(word)

    return total_length / len(words)

# Count paragraphs

def count_paragraphs(text):
    paragraphs = [p for p in text.strip().split("\n\n") if p.strip()]
    return len(paragraphs)

# Count sentences

def count_sentences(text):
    sentences = re.findall(r'[.!?]+', text)
    return len(sentences)


choice = ""

while choice != "0":

    print("\n===== NEWS ARTICLE ANALYZER =====")
    print("1. Count a specific word")
    print("2. Find the most common word")
    print("3. Calculate average word length")
    print("4. Count paragraphs")
    print("5. Count sentences")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        word = input("Enter the word to search: ")
        result = count_specific_word(news_article, word)
        print(f'"{word}" appears {result} time(s).')

    elif choice == "2":
        result = identify_most_common_word(news_article)
        print("Most common word:", result)

    elif choice == "3":
        result = calculate_average_word_length(news_article)
        print(f"Average word length: {result:.2f}")

    elif choice == "4":
        result = count_paragraphs(news_article)
        print("Number of paragraphs:", result)

    elif choice == "5":
        result = count_sentences(news_article)
        print("Number of sentences:", result)

    elif choice == "0":
        print("Program exited successfully.")

    else:
        print("Invalid choice. Please try again.")