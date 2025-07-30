from transformers import pipeline

class QAExtractor:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

    def extract_qa(self, messages):
        questions = []
        answers = []
        for i in range(len(messages) - 1):
            if "?" in messages[i]:
                question = messages[i]
                context = messages[i+1]
                result = self.qa_pipeline(question=question, context=context)
                if result['score'] > 0.5: # You can adjust the confidence threshold
                    questions.append(question)
                    answers.append(result['answer'])
        return questions, answers

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