import re
from collections import Counter

news_article = """
ACME Inc. Unveils Revolutionary Apple Pie Machine, Transforming Baking with Automation

ACME Inc., a leading innovator in culinary technology, has launched a groundbreaking new device that promises to revolutionize the way apple pies are made. Dubbed the “Apple Pie Master,” this machine combines cutting-edge technology with traditional baking techniques to automate the entire pie-making process, ensuring perfect pies every time.

At a press conference held at ACME Inc.'s headquarters in Springfield, the company's CEO, Jane Doe, introduced the Apple Pie Master to an eager audience of journalists, culinary experts, and industry insiders. "Our goal has always been to make cooking and baking accessible and enjoyable for everyone, and with the Apple Pie Master, we are making a giant leap forward," Doe stated.

The Apple Pie Master is designed to simplify the baking process while maintaining the quality and taste of a homemade pie. The machine is equipped with AI-driven sensors that can analyze the quality of ingredients, adjust cooking times, and even replicate intricate baking techniques perfected by master chefs. “This isn't just about saving time; it's about enhancing the baking experience and ensuring consistent results,” Doe explained.

Unpacking the Technology

The heart of the Apple Pie Master lies in its advanced artificial intelligence system. This system is programmed to perform tasks such as peeling and slicing apples, mixing ingredients, and rolling out pie crusts. According to ACME Inc.'s head of product development, Dr. Emily Clark, “The AI not only replicates human actions but learns from each pie made, adjusting its techniques to improve the next one.”

Another innovative feature of the Apple Pie Master is its real-time monitoring capabilities. Cameras and sensors inside the machine provide continuous feedback during the pie-making process, allowing the AI to make micro-adjustments to the temperature and cooking times as needed. This ensures that each pie is baked to golden perfection.

User-Friendly Features

ACME Inc. has designed the Apple Pie Master with user experience in mind. The machine features a sleek, user-friendly interface with pre-programmed settings for different pie recipes. Users can select options for crust type, spice levels, and even the variety of apples they want to use. “We want to cater to all taste preferences, from the traditional to the adventurous,” said marketing director, Tom Nguyen.

The machine also includes a mobile app, allowing users to start the baking process from their smartphones. This app not only controls the machine but also provides users with tips, recipes, and the option to order ingredients directly through ACME Inc.'s partners.

Environmental and Economic Impact

ACME Inc. is also proud of the Apple Pie Master’s environmental credentials. The machine is built from recycled materials and designed to operate with minimal energy consumption. “Sustainability is at the core of all our product designs,” emphasized environmental consultant Lisa Green, who collaborated on the project.

Economically, the Apple Pie Master could have significant implications for both commercial and home bakers. By reducing the time and skill required to make high-quality pies, it opens up new business opportunities for small bakeries and restaurants, and it provides a cost-effective solution for busy consumers who crave homemade desserts without the fuss.

Market Response and Availability

The response to the Apple Pie Master has been overwhelmingly positive. Early adopters and reviewers have praised its ease of use and the quality of the pies it produces. Culinary blogger Mark Spencer commented, “It’s like having a professional baker in your kitchen. The pies are consistently excellent, with perfectly flaky crusts and rich, flavorful fillings.”

ACME Inc. plans to make the Apple Pie Master available online and in select retail stores starting next month. The company has set a competitive price point to make this innovative technology accessible to a broad audience.

The Future of Automated Baking

Looking ahead, ACME Inc. plans to expand its range of automated baking machines. “The Apple Pie Master is just the beginning,” said CEO Jane Doe. “We’re exploring machines for other types of desserts and complex dishes. Our vision is to automate parts of the cooking process without sacrificing the art of cooking.”

The Apple Pie Master from ACME Inc. represents a significant advancement in the field of culinary technology. By automating the process of baking apple pies, this machine not only makes baking more accessible but also sets a new standard for the integration of technology in traditional cooking practices. As more consumers and businesses adopt this technology, it could well redefine our cooking experiences and expectations.
"""


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

    if len(words) == 0:
        return None

    word_counts = Counter(words)

    return word_counts.most_common(1)[0][0]


# Calculate average word length
def calculate_average_word_length(text):
    words = re.findall(r'\b\w+\b', text)

    if len(words) == 0:
        return 0

    total_length = 0

    for word in words:
        total_length += len(word)

    return total_length / len(words)


# Count paragraphs
def count_paragraphs(text):
    if text.strip() == "":
        return 1

    paragraphs = text.split("\n\n")

    count = 0

    for paragraph in paragraphs:
        if paragraph.strip() != "":
            count += 1

    return count


# Count sentences
def count_sentences(text):
    if text.strip() == "":
        return 1

    sentences = re.findall(r"[.!?]", text)

    return len(sentences)


# Main Program
if __name__ == "__main__":

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
            print(count_specific_word(news_article, word))

        elif choice == "2":
            print(identify_most_common_word(news_article))

        elif choice == "3":
            print(calculate_average_word_length(news_article))

        elif choice == "4":
            print(count_paragraphs(news_article))

        elif choice == "5":
            print(count_sentences(news_article))

        elif choice == "0":
            print("Program exited successfully.")

        else:
            print("Invalid choice. Please try again.")