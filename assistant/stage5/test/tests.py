from hstest import StageTest, TestedProgram, CheckResult, dynamic_test


class TestChatBotStageFive(StageTest):
    @dynamic_test
    def test_check_for_openai_imports(self):
        file_path = 'task.py'
        required_strings = ["from openai", "OpenAI(api_key=api_key)"]
        found_strings = {string: False for string in required_strings}

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    for string in required_strings:
                        if string in line:
                            found_strings[string] = True
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return False

        all_found = all(found_strings.values())
        if not all_found:
            CheckResult.wrong("The submission is missing required OpenAI integration lines.")
        return CheckResult.correct()

    @dynamic_test
    def testPersonalizedGreetingAndAdvice(self):
        program = TestedProgram()
        program.start()

        initial_output = program.execute("Alex")
        if "Alex" not in initial_output:
            return CheckResult.wrong("The bot didn't use the user's name in the personalized greeting.")

        user_interest_output = program.execute("I'm interested in learning Python.")
        if len(user_interest_output) == 0:
            return CheckResult.wrong("The bot didn't provide any response to the user's interest in learning Python.")

        return CheckResult.correct()

    @dynamic_test
    def testAgeEstimationAndRecommendations(self):
        program = TestedProgram()
        program.start()

        program.execute("Alex")  # Providing name to the bot
        age_input = "1\n2\n1\n"  # Example remainders when dividing age by 3, 5, and 7
        age_estimation_output = program.execute(age_input)

        if "I estimate you to be around" not in age_estimation_output:
            return CheckResult.wrong("The bot didn't provide an estimated age.")

        if "beginner programming resources." not in age_estimation_output \
                and "intermediate programming tutorials." not in age_estimation_output \
                and "advanced programming concepts." not in age_estimation_output:
            return CheckResult.wrong("The bot didn't provide personalized recommendations based on the estimated age.")

        exit_output = program.execute("exit")
        if "Goodbye, Alex!" not in exit_output:
            return CheckResult.wrong("The bot did not properly say goodbye using the user's name.")

        return CheckResult.correct()

    @dynamic_test
    def test_count_and_interact(self):
        program = TestedProgram()
        program.start()

        # Simulate a conversation to estimate age
        program.execute("Alex")  # Providing name to the bot
        program.execute("1\n2\n1\n")  # Example remainders when dividing age by 3, 5, and 7

        # Test counting up to 10
        count_output = program.execute("10")
        expected_output = '\n'.join(str(i) for i in range(11))
        if expected_output not in count_output and "I'm sorry, I encountered an issue generating a response." not in count_output:
            return CheckResult.wrong("The bot did not count from 0 to 10 correctly.")

        # Test if the bot provides interactive comments or questions
        interactive_comments = ["What do you think about the number 0?",
                                "Can you guess what comes next after 50?"]
        for comment in interactive_comments:
            if comment not in count_output and "I'm sorry, I encountered an issue generating a response." not in count_output:
                return CheckResult.wrong(f"The bot did not provide the expected interactive comment: '{comment}'")

        # Test exit functionality
        exit_output = program.execute("exit")
        if "Goodbye, Alex!" not in exit_output:
            return CheckResult.wrong("The bot did not properly say goodbye using the user's name.")

        return CheckResult.correct()

    @dynamic_test
    def testQuizFunctionality(self):
        program = TestedProgram()
        program.start()

        # Simulate a conversation to estimate age
        program.execute("Alex")  # Providing name to the bot
        program.execute("1\n2\n1\n")  # Example remainders when dividing age by 3, 5, and 7

        program.execute("quiz")  # Start the quiz

        correct_answers = ["Paris", "William Shakespeare", "3.14"]
        user_answers = ["A", "A", "A"]
        quiz_output = ""

        for user_answer, correct_answer in zip(user_answers, correct_answers):
            question_output = program.execute("")  # Skip to receive the question
            quiz_output += question_output + "\n"
            user_input_output = program.execute(user_answer)  # Provide the user's answer
            quiz_output += user_input_output + "\n"

            if "Correct!" in user_input_output:
                correct_output = program.execute("yes")  # Confirm the correct answer
                quiz_output += correct_output + "\n"
            elif "Incorrect!" in user_input_output:
                incorrect_output = program.execute("no")  # Deny the incorrect answer
                quiz_output += incorrect_output + "\n"
        program.execute("exit")
        # Check if the bot presents quiz questions and provides feedback
        # if "Question 1" not in quiz_output or "Question 2" not in quiz_output or "Question 3" not in quiz_output:
        #     return CheckResult.wrong("The bot didn't present all quiz questions.")

        # Check if the bot handles user answers and provides correct feedback
        if "Correct!" not in quiz_output or "Incorrect!" not in quiz_output:
            return CheckResult.wrong("The bot didn't handle user answers and provide feedback correctly.")

        # Check if the bot calculates the score correctly
        if "Quiz completed! You scored" not in quiz_output:
            return CheckResult.wrong("The bot didn't display the quiz completion message with the score.")

        # Check if the bot invites the user to learn more about programming after the quiz
        if "Would you like to learn more about programming?" not in quiz_output:
            return CheckResult.wrong("The bot didn't invite the user to learn more after the quiz.")

        return CheckResult.correct()

    @dynamic_test
    def testExitWithName(self):
        program = TestedProgram()
        program.start()

        program.execute("Alex")

        exit_output = program.execute("exit")
        if "Goodbye" not in exit_output:
            return CheckResult.wrong("The bot did not properly say goodbye using the user's name.")

        return CheckResult.correct()
