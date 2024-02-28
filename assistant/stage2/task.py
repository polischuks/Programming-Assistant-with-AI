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


def main():
    print("Hello! I'm a programming assistant chatbot.")
    name = input("To make our conversation more personal, could you tell me your name? ")
    time_of_day = get_time_of_day()
    print(personalized_greeting(name, time_of_day))

    while True:
        user_input = input(f"{name}: ").lower()
        if user_input == "exit":
            print(f"Goodbye, {name}!")
            break
        else:
            # Assume the user states their interests in the input
            response = get_chat_response(user_input, "programming")
            print(f"Bot: {response}")


if __name__ == "__main__":
    main()
