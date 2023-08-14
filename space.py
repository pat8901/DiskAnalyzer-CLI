import sys
from pypdf import PdfReader
import io

# input = sys.argv[1]
# print(f'You said "{input}"')

pdf = open("Storage_Rep_2023-08-10.pdf", "rb")
reader = PdfReader(pdf)

outputfile = open("temp/full_output.txt", "a")
count = 0
for i in reader.pages:
    page = reader.pages[count]
    text = page.extract_text()
    outputfile.writelines(text + "\n")
    count = count + 1

search_string = "Space Used by Departments"
# search_string = "M EDT 20"
research_output = open("groups/research.txt", "a")
with io.open("temp/full_output.txt", "r") as f:
    for line in f:
        line = line.strip()
        if search_string == line:
            print(f'Found the search string "{line}"')
            break
        else:
            research_output.writelines(line + "\n")


def getTotalStorage():
    print("test")
