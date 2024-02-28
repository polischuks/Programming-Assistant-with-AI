import datetime

def get_time_of_day():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning! My name is Bot, and I'm here to help you with programming. What area of programming are you interested in?"
    elif 12 <= current_hour < 18:
        return "Good afternoon! I'm Bot, and my task is to assist you in learning programming. What areas are you interested in?"
    elif 18 <= current_hour < 22:
        return "Good evening! I'm Bot, your programming assistant. What area would you like to improve your skills in?"
    else:
        return "Good night! I'm here to help you with programming. What area of programming interests you the most?"

def recommend_resources(interests):
    if "web development" in interests:
        return "Great choice! Web development is an exciting field. I recommend starting with learning HTML, CSS, and JavaScript. There's an excellent resource for beginners at [web.dev]."
    elif "artificial intelligence" in interests:
        return "Artificial intelligence opens up many possibilities. I suggest learning Python and libraries like TensorFlow or PyTorch. You can start with courses on [coursera.org]."
    elif "mobile development" in interests:
        return "Mobile development is very popular right now. To begin, I recommend getting familiar with Swift for iOS or Kotlin for Android. You can find an excellent introductory course on [hyperskill.org]."
    elif "databases" in interests:
        return "Databases are the cornerstone of many applications. I suggest starting with SQL, and then moving on to NoSQL databases. You can find a good educational course on [hyperskill.org]."
    else:
        return "I'm sorry, I don't have recommendations for that interest."

def main():
    print("Hello! I'm a programming assistant chatbot.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["hello", "good morning", "good afternoon", "good evening", "good night", "hi"]:
            print(get_time_of_day())
            user_interests = input("You: ").lower()
            print(recommend_resources(user_interests))
        elif user_input.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("I'm not sure how to respond to that. You can say 'hello' to start a conversation or 'exit' to stop.")

if __name__ == "__main__":
    main()
