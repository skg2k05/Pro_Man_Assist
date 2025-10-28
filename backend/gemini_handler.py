import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("⚠️ GEMINI_API_KEY not found in .env file!")

genai.configure(api_key=GEMINI_API_KEY)

# Use the exact model that worked in your Colab session
MODEL_NAME = "gemini-2.0-flash"  # Replace with the one you tested in Colab

def ask_gemini(prompt):
    """
    Generate a response using Gemini API.
    """
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        if hasattr(response, 'text'):
            return response.text.strip()
        else:
            return "⚠️ No text content returned from Gemini API."
    except Exception as e:
        return f"❌ Gemini API Error: {str(e)}"
