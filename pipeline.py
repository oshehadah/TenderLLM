
import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader
from PIL import Image
import re

def ocr_extract_text(pdf_path):
    images = convert_from_path(pdf_path, dpi=300)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img, lang='ara')
    return text

def pdf_extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = "\n".join([page.extract_text() or "" for page in reader.pages])
    return text

def preprocess_text(text):
    return text.replace("\u200f", "").replace("\xa0", " ").strip()

def extract_fields(text):
    fields = {}
    def find(pattern, key):
        match = re.search(pattern, text)
        if match:
            fields[key] = match.group(1).strip()
    find(r"اسم المنافسة\s*[:：]?\s*(.+)", "project_name")
    find(r"رقم المنافسة\s*[:：]?\s*(.+)", "tender_number")
    find(r"تاريخ الطرح\s*[:：]?\s*(.+)", "release_date")
    find(r"آخر موعد لتقديم العروض\s*[:：]?\s*(.+)", "submission_deadline")
    find(r"تاريخ فتح العروض\s*[:：]?\s*(.+)", "opening_date")
    find(r"مدة العقد\s*[:：]?\s*(.+)", "contract_duration")
    find(r"مكان تنفيذ الأعمال\s*[:：]?\s*(.+)", "execution_location")
    find(r"الجهة المستفيدة\s*[:：]?\s*(.+)", "beneficiary")
    return fields

def summarize(text):
    lines = text.splitlines()
    summary_lines = [line.strip() for line in lines if 10 < len(line.strip()) < 120]
    return "\n".join(summary_lines[:10])

def run_pipeline(pdf_path):
    try:
        text = pdf_extract_text(pdf_path)
        if len(text.strip()) < 50:
            text = ocr_extract_text(pdf_path)
    except Exception:
        text = ocr_extract_text(pdf_path)
    clean = preprocess_text(text)
    fields = extract_fields(clean)
    summary = summarize(clean)
    return {"summary": summary, "structured": fields}
