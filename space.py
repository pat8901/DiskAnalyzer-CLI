import sys
from pypdf import PdfReader
import csv


def main():
    # input = sys.argv[1]
    # print(f'You said "{input}"')
    createFullOutput()
    # createResearchOutput()
    createResearchOutputTest()
    createDepartmentOutput()
    createCollegesOutput()
    # convertToCSV()
    # convertToCSVTest()
    listLine()
    convert()
    csvWriter()


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


def createResearchOutputTest():
    begin = "-------------------------------   -------    ------------    ------------    ------------    --------------"
    end = "=========================================|===============|===============|===============|=================|"
    beginFound = False
    with open("temp/full_output.txt", "r") as f_input:
        with open("groups/research_test.txt", "w") as f_output:
            for line in f_input:
                if end in line:
                    break
                if beginFound:
                    line = line.strip()
                    f_output.write(line + "\n")
                elif begin in line:
                    beginFound = True


def createDepartmentOutput():
    header = "                                            Space Used by Departments"
    begin = "-----------------------------------------    ------------    ------------    ------------    --------------"
    end = "=========================================|===============|===============|===============|=================|"
    headerFound = False
    beginFound = False
    with open("temp/full_output.txt", "r") as f_input:
        with open("groups/departments.txt", "w") as f_output:
            for line in f_input:
                if header in line:
                    headerFound = True
                if headerFound:
                    if end in line:
                        break
                    elif beginFound:
                        line = line.strip()
                        f_output.write(line + "\n")
                    elif begin in line:
                        beginFound = True


def createCollegesOutput():
    header = "                                            Space Used by Colleges"
    begin = "-----------------------------------------    ------------    ------------    ------------    --------------"
    end = "=========================================|===============|===============|===============|=================|"
    headerFound = False
    beginFound = False
    with open("temp/full_output.txt", "r") as f_input:
        with open("groups/colleges.txt", "w") as f_output:
            for line in f_input:
                if header in line:
                    headerFound = True
                if headerFound:
                    if end in line:
                        break
                    elif beginFound:
                        line = line.strip()
                        f_output.write(line + "\n")
                    elif begin in line:
                        beginFound = True


def listLine():
    with open("groups/research_test.txt", "r") as f:
        with open("temp/test.txt", "w") as f_out:
            content = f.readlines()
            line = content[0]
            line = line.split("|")
            for i in line:
                string = i.strip()
                # string = i.replace(" ", ",")
                print(string)
                f_out.write(string + ",")


# Best working to csv so far
def convert():
    with open("groups/research_test.txt", "r") as f:
        with open("temp/test_full.txt", "w") as f_out:
            for line in f:
                line = line.split("|")
                for word in line:
                    string = word.strip()
                    # string = i.replace(" ", ",")
                    print(string)
                    f_out.write(string + ",")
                # f_out.write("\n")


def csvWriter():
    with open("groups/research_test.txt", "r") as f:
        with open("temp/test.csv", "w", newline="") as file:
            for line in f:
                line = line.split("|")
                writer = csv.writer(file)
                writer.writerow(line)


def getTotalStorage():
    print("test")


if __name__ == "__main__":
    main()
