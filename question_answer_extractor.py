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

