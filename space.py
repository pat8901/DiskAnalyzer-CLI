# Note
# Add headers to csv files?
#
import sys
from pypdf import PdfReader
import csv
import pandas as pd
import matplotlib as plt


def main():
    # input = sys.argv[1]
    # print(f'You said "{input}"')

    createFullOutput()
    createResearchOutput()
    createDepartmentOutput()
    createCollegesOutput()

    csvWriter("research", "research")
    csvWriter("departments", "departments")
    csvWriter("colleges", "colleges")

    getTotalStorage()


def createFullOutput():
    pdf = open("Storage_Rep_2023-08-10.pdf", "rb")
    reader = PdfReader(pdf)
    with open("tmp/full_output.txt", "w") as f_output:
        count = 0
        for i in reader.pages:
            page = reader.pages[count]
            text = page.extract_text()
            f_output.write(text + "\n")
            count = count + 1


# def createResearchOutput():
#     search_string = "Space Used by Departments"
#     # search_string = "M EDT 20"
#     with open("temp/full_output.txt", "r") as f_input:
#         with open("groups/research.txt", "w") as f_output:
#             for line in f_input:
#                 line = line.strip()
#                 if search_string in line:
#                     print(f'Found the search string "{line}"')
#                     break
#                 else:
#                     f_output.write(line + "\n")


def createResearchOutput():
    begin = "-------------------------------   -------    ------------    ------------    ------------    --------------"
    end = "=========================================|===============|===============|===============|=================|"
    beginFound = False
    with open("tmp/full_output.txt", "r") as f_input:
        with open("groups/research.txt", "w") as f_output:
            for line in f_input:
                if end in line:
                    break
                if beginFound:
                    line = line.strip()
                    line = line[:-1]
                    f_output.write(line + "\n")
                elif begin in line:
                    beginFound = True


def createDepartmentOutput():
    header = "                                            Space Used by Departments"
    begin = "-----------------------------------------    ------------    ------------    ------------    --------------"
    end = "=========================================|===============|===============|===============|=================|"
    headerFound = False
    beginFound = False
    with open("tmp/full_output.txt", "r") as f_input:
        with open("groups/departments.txt", "w") as f_output:
            for line in f_input:
                if header in line:
                    headerFound = True
                if headerFound:
                    if end in line:
                        break
                    elif beginFound:
                        line = line.strip()
                        line = line[:-1]
                        f_output.write(line + "\n")
                    elif begin in line:
                        beginFound = True


def createCollegesOutput():
    header = "                                            Space Used by Colleges"
    begin = "-----------------------------------------    ------------    ------------    ------------    --------------"
    end = "=========================================|===============|===============|===============|=================|"
    headerFound = False
    beginFound = False
    with open("tmp/full_output.txt", "r") as f_input:
        with open("groups/colleges.txt", "w") as f_output:
            for line in f_input:
                if header in line:
                    headerFound = True
                if headerFound:
                    if end in line:
                        break
                    elif beginFound:
                        line = line.strip()
                        line = line[:-1]
                        f_output.write(line + "\n")
                    elif begin in line:
                        beginFound = True


def csvWriter(input, output):
    with open(f"groups/{input}.txt", "r") as f:
        with open(f"csv/{output}.csv", "w", newline="") as file:
            writer = csv.writer(file)
            if output == "research":
                headers = [
                    "Full Name",
                    "DepCode",
                    "AFS Groups",
                    "Users AFS",
                    "Users Panas.",
                    "Tot.Used Space",
                ]
                writer.writerow(headers)
            if output == "departments":
                headers = [
                    "Department",
                    "AFS Groups",
                    "Users AFS",
                    "Users Panas.",
                    "Tot.Used Space",
                ]
                writer.writerow(headers)
            if output == "colleges":
                headers = [
                    "College Name",
                    "AFS Groups",
                    "Users AFS",
                    "Users Panas.",
                    "Tot.Used Space",
                ]
                writer.writerow(headers)
            for line in f:
                trimmedWords = []
                line = line.split("|")
                for word in line:
                    new_word = word.strip()
                    trimmedWords.append(new_word)
                # writer = csv.writer(file)
                writer.writerow(trimmedWords)


def getTotalStorage():
    total = 0
    df = pd.read_csv("csv/research.csv")
    total = df["Tot.Used Space"].sum()
    terabyte = total / 1000000000
    print(f"Total Storage (KB): {total}")
    print(f"Total Storage (TB): {terabyte}")


if __name__ == "__main__":
    main()
