import sys
from pypdf import PdfReader

# input = sys.argv[1]
# print(f'You said "{input}"')

pdf = open("Storage_Rep_2023-08-10.pdf", "rb")
reader = PdfReader(pdf)

outputfile = open("./storage_output.txt", "a")
count = 0
for i in reader.pages:
    page = reader.pages[count]
    text = page.extract_text()
    outputfile.writelines(text + "\n")
    count = count + 1
