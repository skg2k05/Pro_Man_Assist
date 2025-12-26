# Pro_Man_Assist 🤖📘  
**Product Manual Assistant using Gemini API & Streamlit**

Pro_Man_Assist is a lightweight **Generative AI chatbot** that helps users ask questions directly from a **product manual** (PDF or document).  
It demonstrates the **basic Retrieval-Augmented Generation (RAG)** concept using **Google Gemini API** and a **Streamlit-based UI**.

Users upload a product manual, ask questions related to it, and get accurate answers grounded in the uploaded document.

---

## 🔍 Project Overview

- Upload a **product manual file**
- Extract relevant content from the document
- Ask natural language questions
- Get AI-generated answers based **only on the manual**
- Simple UI built using **Streamlit**
- Uses **Gemini API** for LLM responses

This project is meant for **learning and demonstration purposes** to understand how RAG works in real-world GenAI applications.

---

## 🧠 Key Concepts Used

- **Retrieval-Augmented Generation (RAG)**
- **Document-based Question Answering**
- **Google Gemini API**
- **Streamlit UI**
- **Text Embedding & Context Injection**

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini API**
- **LangChain / Text processing utilities**
- **PDF / Document loaders**

---

## 🚀 How It Works

1. User uploads a product manual (PDF)
2. The document is processed and split into chunks
3. Relevant context is retrieved based on user query
4. Gemini model generates an answer using retrieved context
5. Answer is displayed on the Streamlit UI

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository 

git clone https://github.com/skg2k05/Pro_Man_Assist.git
cd Pro_Man_Assist

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt

--- 

### 🔑 Getting Your Google Gemini API Key (Free)

Go to Google AI Studio
👉 https://aistudio.google.com/

1.Sign in with your Google account
2.Click on Get API Key
3.Create a new API key
4.Copy the API key for use in the project

### 🔐 Configure API Key
Create a .env file in the project root and add:
GOOGLE_API_KEY=your_gemini_api_key_here

### ▶️ Run the Application
streamlit run app.py
The app will open in your browser (usually at http://localhost:8501).

--- 

### 🧪 How to Use

Upload a product manual file
Wait for document processing
Ask questions related to the product
Get accurate, context-aware answers

### 📚 Learning Purpose

This project is ideal for:
-- Beginners exploring GenAI
-- Understanding RAG pipelines
-- Learning LLM + document interaction
-- Streamlit-based AI app development
