import datetime
from openai import OpenAI

api_key = "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"
client = OpenAI(api_key=api_key)


def get_time_of_day():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        time_of_day = "morning"
    elif 12 <= current_hour < 18:
        time_of_day = "afternoon"
    elif 18 <= current_hour < 22:
        time_of_day = "evening"
    else:
        time_of_day = "night"
    return time_of_day


def personalized_greeting(name, time_of_day):
    greetings = {
        "morning": f"Good morning, {name}! How can I assist you with programming today?",
        "afternoon": f"Good afternoon, {name}! What programming topics are you interested in?",
        "evening": f"Good evening, {name}! What would you like to learn in programming tonight?",
        "night": f"Good night, {name}. Looking for some programming advice before bed?"
    }
    return greetings[time_of_day]


def get_chat_response(question, user_interests):
    try:
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            temperature=0.5,
            messages=[
                {
                    "role": "user",
                    "content": f"This is a chatbot that helps people with programming based on their interests. The user is interested in {user_interests}. They asked: {question}"
                }
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return "I'm sorry, I encountered an issue generating a response. Please try asking something else."


def estimate_age():
    print("To provide you with personalized recommendations, I'll need to estimate your age.")
    age_remainders = []

    while len(age_remainders) < 3:  # Continue asking for remainders until we have 3
        user_input = input("When you divide your age by 3, what is the remainder? ").lower()
        if user_input == "exit":  # Check if the user wants to exit
            print("Goodbye!")
            exit()  # Exit the program
        try:
            age_remainders.append(int(user_input))
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Implementing Chinese Remainder Theorem to estimate age
    # Using simple brute-force approach as an example
    for age in range(1, 100):
        if all(age % prime == remainder for prime, remainder in zip([3, 5, 7], age_remainders)):
            return age


def count_and_interact(number):
    for i in range(number + 1):
        if i % 10 == 0:
            # Generate an interesting comment or question using ChatGPT API
            response = get_chat_response(f"What do you think about the number {i}?", "numbers")
            print(f"Bot: {response}")

            # Offer an interactive task related to numbers
            if i == 50:
                print("Can you guess what comes next after 50?")
                user_guess = input("Your guess: ")
                if user_guess.strip().lower() == "51":
                    print("Correct!")
                else:
                    print("Incorrect. Keep counting!")

        print(i)


def main():
    print("Hello! I'm a programming assistant chatbot.")
    name = input("To make our conversation more personal, could you tell me your name? ")
    time_of_day = get_time_of_day()
    print(personalized_greeting(name, time_of_day))

    estimated_age = estimate_age()  # Estimate user's age

    print(f"I estimate you to be around {estimated_age} years old.")
    # Leveraging the guessed age for personalized recommendations
    if estimated_age < 20:
        print("You seem young! Here are some beginner programming resources.")
    elif 20 <= estimated_age < 40:
        print("You're in your prime learning years! Check out these intermediate programming tutorials.")
    else:
        print("You have a wealth of experience! Here are some advanced programming concepts.")

    while True:
        user_input = input(f"{name}: ").lower()
        if user_input == "exit":
            print(f"Goodbye, {name}!")
            break  # Exit the loop and end the program
        else:
            # Assume the user states their interests in the input
            response = get_chat_response(user_input, "programming")
            if "I'm sorry, I encountered an issue generating a response." in response:
                print(f"Bot: {response}")
            else:
                print(f"Bot: {response}")

        if "quiz" in user_input:
            start_quiz()  # Start the quiz


def start_quiz():
    print("Welcome to the programming quiz!")
    questions = [
        "What is the process of finding and correcting errors in a program called?",
        "What programming language is known for its flexibility and use in web development?",
        "Which data structure follows the Last In, First Out (LIFO) principle?",
        "In object-oriented programming, what term refers to creating new instances of a class?",
        "What does the acronym 'SQL' stand for?"
    ]
    answers = [
        {"A": "Debugging", "B": "Compiling", "C": "Linking", "D": "Executing"},
        {"A": "Python", "B": "C++", "C": "JavaScript", "D": "Java"},
        {"A": "Queue", "B": "Stack", "C": "Linked List", "D": "Array"},
        {"A": "Instantiation", "B": "Declaration", "C": "Definition", "D": "Assignment"},
        {"A": "Structured Query Language", "B": "Sequential Query Language", "C": "Simple Query Language",
         "D": "Standard Query Language"}
    ]
    correct_answers = ["A", "C", "B", "A", "A"]

    score = 0
    for i in range(len(questions)):
        print(f"Question {i + 1}: {questions[i]}")
        print("Options:")
        for option, answer in answers[i].items():
            print(f"{option}. {answer}")
        user_answer = input("Your answer: ").upper()
        if user_answer == correct_answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print(f"Quiz completed! You scored {score} out of {len(questions)}.")

    additional_learning = input("Would you like to learn more about programming? (yes/no): ").lower()
    if additional_learning == "yes":
        print("Here are some additional learning resources.")
    else:
        print("Okay. Goodbye!")


if __name__ == "__main__":
    main()
