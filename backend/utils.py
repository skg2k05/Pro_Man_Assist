# backend/utils.py

def build_priority_prompt(question, pdf_text, web_text=None):
    """
    Builds a prompt for the Gemini LLM.
    Ensures PDF is primary, website used only if PDF doesn't fully answer.
    """
    prompt = f"""
You are an AI assistant answering questions about the product ZEB-SPACE DECK PRO.

PDF Manual Content:
{pdf_text}

Website Content:
{web_text if web_text else 'No website content provided.'}

Instructions:
1. Answer using the PDF content ONLY if it fully answers the question.
2. If the PDF does NOT contain the information, use the website content to answer.
3. Do NOT rely on the PDF if the answer is missing or incomplete.
4. Be concise, straight to the point, and avoid unnecessary scrolling.
5. If neither source provides the answer, reply: "Information not available in the manual or website."

Question:
{question}

Answer:
"""
    return prompt
