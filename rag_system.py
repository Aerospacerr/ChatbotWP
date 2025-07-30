from data_loader import DataLoader
from web_scraper import WebScraper
from question_answer_extractor import QAExtractor


class RAGSystem:
    def __init__(self, chat_file):
        self.loader = DataLoader(chat_file)
        self.scraper = WebScraper()
        self.extractor = QAExtractor()

    def verify_answers(self):
        # Load and preprocess chat data
        data = self.loader.load_data()
        messages = self.loader.preprocess_data(data)

        # Extract URLs from messages
        links = self.loader.extract_links(messages)

        # Fetch and scrape web data
        web_data = []
        for link in links:
            html = self.scraper.fetch_page(link)
            if html:
                content = self.scraper.scrape_content(html)
                web_data.append(content)

        # Extract questions and answers from chat
        questions, answers = self.extractor.extract_qa(messages)

        # Verify answers with web data (simplified)
        verified_answers = []
        for answer in answers:
            for content in web_data:
                if answer in content:
                    verified_answers.append((answer, True))
                    break
            else:
                verified_answers.append((answer, False))

        return verified_answers


if __name__ == "__main__":
    rag_system = RAGSystem("/Users/emircan/Desktop/Case_Study/ChatbotWP/_chat.txt")
    results = rag_system.verify_answers()
    for answer, is_correct in results:
        print(f"Answer: {answer} | Correct: {is_correct}")
