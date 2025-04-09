
from pipeline import run_pipeline
import sys
import json

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py path/to/tender.pdf")
        return
    pdf_path = sys.argv[1]
    result = run_pipeline(pdf_path)
    print("\n📄 Summary:\n")
    print(result["summary"])
    print("\n📦 Structured Output:\n")
    print(json.dumps(result["structured"], ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
