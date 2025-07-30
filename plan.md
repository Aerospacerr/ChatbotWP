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

-   **Goal:** More accurately identify question-answer pairs from the chat log.
-   **Method:** Use a pre-trained NLP model for question-answering to extract questions and their corresponding answers.

### 2. Implement Semantic Search

-   **Goal:** Find more relevant information from the scraped web content.
-   **Method:**
    -   Vectorize the scraped web content and the extracted answers using a sentence transformer model.
    -   Use a vector store (e.g., FAISS, Chroma) to perform similarity searches.

### 3. Add a Generation Component

-   **Goal:** Generate new, more comprehensive answers based on the retrieved context.
-   **Method:** Integrate a large language model (LLM) to generate answers.

### 4. Refactor the Code

-   **Goal:** Improve the project's structure and maintainability.
-   **Method:**
    -   Create a `main.py` as the single entry point.
    -   Modularize the existing components.
    -   Use a `config.py` for managing settings.

## Progress

### Step 1: Improve Question-Answer Extraction (Done)

- [x] Update `question_answer_extractor.py` to use a pre-trained NLP model.

### Step 2: Implement Semantic Search (Done)

- [x] Vectorize documents and answers.
- [x] Implement similarity search using a vector store.

### Step 3: Add a Generation Component (Done)

- [x] Integrate a large language model (LLM) to generate answers.

### Step 4: Refactor the Code (In Progress)

- [x] Create a `main.py` as the single entry point.
- [x] Modularize the existing components.
- [x] Use a `config.py` for managing settings.
