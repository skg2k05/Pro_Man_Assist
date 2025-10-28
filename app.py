import streamlit as st
from backend.pdf_processor import extract_pdf_text_with_ocr
from backend.web_scraper import scrape_website
from backend.utils import build_priority_prompt
from backend.gemini_handler import ask_gemini
import tempfile
import time

st.set_page_config(page_title="Product Manual Assistant", page_icon="🤖")

st.title("🤖Product Manual Assistant")
st.caption("Upload a product manual or provide a website link — then ask questions to get real-time answers powered by Gemini.")

# Initialize chat log in session
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# Upload PDF section
uploaded_pdf = st.file_uploader("📄 Upload PDF Manual", type=["pdf"])
website_link = st.text_input("🌐 Optional: Enter product website link")

if uploaded_pdf:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_pdf.read())
        pdf_path = tmp.name

    st.success("✅ PDF uploaded successfully! Extracting text...")

    start_time = time.time()
    with st.spinner("🔍 Extracting text from PDF... This may take a while."):
        pdf_text = extract_pdf_text_with_ocr(pdf_path)
    end_time = time.time()
    elapsed = end_time - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    st.info(f"✅ Extraction complete in {minutes}m {seconds}s")
else:
    pdf_text = None

st.divider()

# Ask question
query = st.text_input("💬 Ask a question about your product manual")

if st.button("Get Answer"):
    if not query.strip():
        st.warning("Please enter a question.")
    elif not pdf_text:
        st.error("Please upload a PDF first.")
    else:
        st.info("🧠 Generating answer... please wait.")

        # Extract website text if link provided
        web_text = scrape_website(website_link) if website_link else None

        # Build prompt with PDF priority, website fallback
        prompt = build_priority_prompt(query, pdf_text, web_text)

        # Call Gemini API
        answer = ask_gemini(prompt)

        # Save to chat log
        st.session_state.chat_log.append({"question": query, "answer": answer})

        # Display current answer
        st.subheader("🧠 Answer:")
        st.write(answer)
        st.divider()

# Display chat log
if st.session_state.chat_log:
    st.subheader("📜 Chat Log")
    for entry in st.session_state.chat_log:
        st.markdown(f"**Q:** {entry['question']}")
        st.markdown(f"**A:** {entry['answer']}")
        st.divider()

# Clear chat log button
if st.button("Clear Chat"):
    st.session_state.chat_log = []
    st.experimental_rerun()

# to run this file , give command  streamlit run app.py