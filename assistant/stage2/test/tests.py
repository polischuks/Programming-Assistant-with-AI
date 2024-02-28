from hstest import StageTest, TestedProgram, CheckResult, dynamic_test


class TestChatBotStageTwo(StageTest):
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
    def testExitWithName(self):
        program = TestedProgram()
        program.start()

        program.execute("Alex")

        exit_output = program.execute("exit")
        if "Goodbye, Alex!" not in exit_output:
            return CheckResult.wrong("The bot did not properly say goodbye using the user's name.")

        return CheckResult.correct()


