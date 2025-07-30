class QAExtractor:
    def __init__(self):
        self.questions = []
        self.answers = []

    def extract_qa(self, messages):
        for message in messages:
            if "?" in message:
                self.questions.append(message)
            else:
                self.answers.append(message)
        return self.questions, self.answers


if __name__ == "__main__":
    extractor = QAExtractor()
    sample_messages = [
        "How are you?",
        "I'm fine, thank you!",
        "What is the capital of France?",
        "Paris is the capital of France.",
    ]
    questions, answers = extractor.extract_qa(sample_messages)
    print("Questions:", questions)
    print("Answers:", answers)
