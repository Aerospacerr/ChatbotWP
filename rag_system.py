from data_loader import DataLoader
from web_scraper import WebScraper
from question_answer_extractor import QAExtractor
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class RAGSystem:
    def __init__(self, chat_file):
        self.loader = DataLoader(chat_file)
        self.scraper = WebScraper()
        self.extractor = QAExtractor()
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

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

        # Create embeddings for web data
        web_data_embeddings = self.embedding_model.encode(web_data, convert_to_tensor=True)

        # Create a FAISS index
        index = faiss.IndexFlatL2(web_data_embeddings.shape[1])
        index.add(web_data_embeddings.cpu().detach().numpy())

        # Verify answers with web data using similarity search
        verified_answers = []
        for answer in answers:
            answer_embedding = self.embedding_model.encode([answer], convert_to_tensor=True)
            distances, indices = index.search(answer_embedding.cpu().detach().numpy(), 1)
            if distances[0][0] < 1.0:  # You can adjust the distance threshold
                verified_answers.append((answer, True, web_data[indices[0][0]]))
            else:
                verified_answers.append((answer, False, None))

        return verified_answers

if __name__ == "__main__":
    rag_system = RAGSystem("/Users/emircan/Desktop/Case_Study/ChatbotWP/_chat.txt")
    results = rag_system.verify_answers()
    for answer, is_correct, context in results:
        print(f"Answer: {answer} | Correct: {is_correct}")
        if is_correct:
            print(f"Context: {context}")