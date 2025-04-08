import PyPDF2

# Read the PDF file
pdf_path = "2503.18102v1.pdf"
pdf = PyPDF2.PdfReader(pdf_path)
text = ""

# Extract text from each page
for i, page in enumerate(pdf.pages):
    page_text = page.extract_text()
    if page_text:
        text += f"\n\n--- Page {i+1} ---\n\n{page_text}"

# Write the text to a file
with open("paper_text.txt", "w", encoding="utf-8") as f:
    f.write(text)

print(f"Extracted text from {len(pdf.pages)} pages and saved to paper_text.txt")
