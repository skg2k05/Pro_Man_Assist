import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

def extract_pdf_text_with_ocr(file_path):
    """
    Extracts text from a PDF.
    Falls back to OCR if the page contains images (e.g., scanned manual).
    """
    doc = fitz.open(file_path)
    text = ""

    for page_num, page in enumerate(doc, start=1):
        page_text = page.get_text("text")
        if page_text.strip():
            text += f"\n--- Page {page_num} ---\n{page_text}"
        else:
            pix = page.get_pixmap()
            img = Image.open(io.BytesIO(pix.tobytes()))
            ocr_text = pytesseract.image_to_string(img)
            text += f"\n--- Page {page_num} (OCR) ---\n{ocr_text}"
    return text
