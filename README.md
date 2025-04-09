
# TenderLLM: Automated Arabic Tender Document Analyzer

This repository contains the source code, sample input, and detailed execution instructions for TenderLLM, as described in the submitted SoftwareX manuscript.

## What is TenderLLM?

TenderLLM is a lightweight, rule-based system that extracts structured data and human-readable summaries from Arabic government tender PDFs — including scanned documents. It combines:

- OCR (via Tesseract)
- PDF text extraction (via PyPDF2)
- Regex filters
- JSON output + summaries

## Repository Contents

- pipeline.py – Core logic
- main.py – CLI interface
- samples/tender_1.pdf – Sample Arabic tender
- README.md – Documentation
- LICENSE – MIT License

## How to Run

```bash
pip install pytesseract pdf2image PyPDF2 pillow
python main.py samples/tender_1.pdf
```
