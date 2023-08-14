import sys
from pypdf import PdfReader

input = sys.argv[1]
print(f'You said "{input}"')

pdf = open("Storage_Rep_2023-08-10.pdf", "rb")
reader = PdfReader(pdf)
number_pages = len(reader.pages)

print(f"Number of pages: {number_pages}")

page0 = reader.pages[0]
page1 = reader.pages[1]
page0text = page0.extract_text()
page1text = page1.extract_text()
print(page0text)
print(page1text)
