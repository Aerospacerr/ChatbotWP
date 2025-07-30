# Project Improvement Plan

This document outlines the plan for improving the RAG chatbot project.

## Initial Analysis

The project is a basic RAG system that extracts questions and answers from a chat log and verifies them against web content.

**Limitations:**

*   Naive question-answer extraction.
*   Simple substring-based answer verification.
*   No generative component.
*   No semantic search.

## Improvement Plan

### 1. Improve Question-Answer Extraction

The current method of identifying questions is very basic. We can improve this by using a more sophisticated approach, such as a pre-trained NLP model, to identify question-answer pairs more accurately.

**Our Plan:**

*   Use a pre-trained question-answering model (like one from the Hugging Face Hub) to identify questions and their corresponding answers in the chat log.

### 2. Implement Semantic Search

Currently, the system checks for the exact answer text in the scraped web content. This is not very effective. We can significantly improve this by using semantic search.

**Our Plan:**

*   **Vectorize Documents:** We'll use a sentence transformer model to create vector embeddings of the scraped web content.
*   **Vectorize Answers:** We'll do the same for the answers extracted from the chat.
*   **Implement Similarity Search:** We'll use a vector store (like FAISS or Chroma) to perform a similarity search between the answer vectors and the web content vectors. This will allow us to find semantically similar content, even if the wording isn't an exact match.

### 3. Add a Generation Component

A true RAG system doesn't just retrieve information; it generates an answer based on the retrieved context. We can add a language model to do this.

**Our Plan:**

*   **Integrate a Language Model:** We'll use a language model (like one from OpenAI or a local model) to generate a new, more comprehensive answer based on the original answer and the context retrieved from the web.

### 4. Refactor the Code

We can improve the code's structure and organization to make it more modular and easier to maintain.

**Our Plan:**

*   **Create a `main.py`:** We'll create a main.py file to be the single entry point for the application.
*   **Modularize Components:** We'll break down the existing classes into smaller, more focused modules.
*   **Add a `config.py`:** We'll use a configuration file to manage settings like API keys and model names.

## Progress

### Step 1: Improve Question-Answer Extraction (Done)

- [x] Update `question_answer_extractor.py` to use a pre-trained NLP model.
- [x] Update `requirements.txt` with new dependencies.

### Step 2: Implement Semantic Search (Up Next)

- [ ] Vectorize documents and answers.
- [ ] Implement similarity search using a vector store.
