from hstest import StageTest, TestedProgram, CheckResult, dynamic_test


class TestChatBot(StageTest):

    @dynamic_test(data=[
        ("I'm interested in web development.", "HTML, CSS, and JavaScript"),
        ("Artificial intelligence.", "Python and libraries like TensorFlow or PyTorch"),
        ("Mobile development.", "Swift for iOS or Kotlin for Android"),
        ("Databases.", "SQL, and then moving on to NoSQL databases")
    ])
    def testUserInterests(self, user_input, expected_in_output):
        program = TestedProgram()
        program.start()
        # Пропускаем начальное приветствие
        program.execute("hello")

        output = program.execute(user_input)
        if expected_in_output not in output:
            return CheckResult.wrong(
                f"Expected to find '{expected_in_output}' in the output for input '{user_input}', but got: {output}")

        return CheckResult.correct()

    @dynamic_test
    def testExit(self):
        program = TestedProgram()
        program.start()
        output = program.execute("exit")
        if "Goodbye!" not in output:
            return CheckResult.wrong("Expected 'Goodbye!' after entering 'exit'.")
        return CheckResult.correct()
