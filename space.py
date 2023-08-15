import sys
from pypdf import PdfReader


def main():
    # input = sys.argv[1]
    # print(f'You said "{input}"')
    createFullOutput()
    createResearchOutput()
    # convertToCSV()
    convertToCSVTest()


def createFullOutput():
    pdf = open("Storage_Rep_2023-08-10.pdf", "rb")
    reader = PdfReader(pdf)
    with open("temp/full_output.txt", "w") as f_output:
        # outputfile = open("temp/full_output.txt", "a")
        count = 0
        for i in reader.pages:
            page = reader.pages[count]
            text = page.extract_text()
            f_output.write(text + "\n")
            count = count + 1


def createResearchOutput():
    search_string = "Space Used by Departments"
    # search_string = "M EDT 20"
    with open("temp/full_output.txt", "r") as f_input:
        with open("groups/research.txt", "w") as f_output:
            for line in f_input:
                line = line.strip()
                if search_string in line:
                    print(f'Found the search string "{line}"')
                    break
                else:
                    f_output.write(line + "\n")


def convertToCSV():
    with open("groups/research.txt", "r") as f_input:
        with open("temp/test.txt", "w") as f_output:
            for line in f_input:
                line = line.strip()
                " ".join(line.split())
                f_output.write(line + "\n")


def convertToCSVTest():
    with open("groups/research.txt", "r") as f_input:
        with open("temp/test.txt", "w") as f_output:
            content = f_input.readlines()
            # print(content[5])
            # for line in f_input:
            #     line = line.strip()
            #     " ".join(line.split())
            f_output.write(content[4])


def getTotalStorage():
    print("test")


if __name__ == "__main__":
    main()
