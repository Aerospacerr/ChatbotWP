import os
from dotenv import load_dotenv

from config import CHAT_FILE_PATH, GOOGLE_API_KEY_ENV_VAR
from data_loader import DataLoader
from web_scraper import WebScraper
from question_answer_extractor import QAExtractor
from rag_system import RAGSystem

def main():
    load_dotenv()
    google_api_key = os.getenv(GOOGLE_API_KEY_ENV_VAR)

    if not google_api_key:
        print("Error: GOOGLE_API_KEY not found in environment variables.")
        return

    rag_system = RAGSystem(CHAT_FILE_PATH, google_api_key)
    results = rag_system.verify_answers()

    for answer, is_correct, context, new_answer in results:
        print(f"Answer: {answer} | Correct: {is_correct}")
        if is_correct:
            print(f"Context: {context}")
            print(f"New Answer: {new_answer}")

if __name__ == "__main__":
    main()
