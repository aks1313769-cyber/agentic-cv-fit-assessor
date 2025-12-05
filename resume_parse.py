from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    try:
        return extract_text(pdf_path)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""
