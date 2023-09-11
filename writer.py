import sys
from pypdf import PdfReader
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tools


# +======================================================================================+
# |           Converts input pdf into a txt file to be used in further processing        |
# |                           *Can be optimized further*                                 |
# +======================================================================================+
def createFullOutput(input, date):
    pdf = open(f"{input}", "rb")
    reader = PdfReader(pdf)
    with open(f"text/full_output/full_output_{date}.txt", "w") as f_output:
        count = 0
        for i in reader.pages:
            page = reader.pages[count]
            text = page.extract_text()
            f_output.write(text + "\n")
            count = count + 1


# +======================================================================================+
# |           Converts input pdf into a txt file to be used in further processing        |
# |                           *Can be optimized further*                                 |
# +======================================================================================+
def createResearchOutput(date):
    begin = "-------------------------------   -------    ------------    ------------    ------------    --------------"
    end = "=========================================|===============|===============|===============|=================|"
    beginFound = False
    with open(f"text/full_output/full_output_{date}.txt", "r") as f_input:
        with open(f"text/grouped_output/research_{date}.txt", "w") as f_output:
            for line in f_input:
                if end in line:
                    break
                if beginFound:
                    line = line.strip()
                    line = line[:-1]
                    f_output.write(line + "\n")
                elif begin in line:
                    beginFound = True


# +======================================================================================+
# |           Converts input pdf into a txt file to be used in further processing        |
# |                           *Can be optimized further*                                 |
# +======================================================================================+
def createDepartmentOutput(date):
    header = "                                            Space Used by Departments"
    begin = "-----------------------------------------    ------------    ------------    ------------    --------------"
    end = "=========================================|===============|===============|===============|=================|"
    headerFound = False
    beginFound = False
    with open(f"text/full_output/full_output_{date}.txt", "r") as f_input:
        with open(f"text/grouped_output/departments_{date}.txt", "w") as f_output:
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


# +======================================================================================+
# |           Converts input pdf into a txt file to be used in further processing        |
# |                           *Can be optimized further*                                 |
# +======================================================================================+
def createCollegesOutput(date):
    header = "                                            Space Used by Colleges"
    begin = "-----------------------------------------    ------------    ------------    ------------    --------------"
    end = "=========================================|===============|===============|===============|=================|"
    headerFound = False
    beginFound = False
    with open(f"text/full_output/full_output_{date}.txt", "r") as f_input:
        with open(f"text/grouped_output/colleges_{date}.txt", "w") as f_output:
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


# +======================================================================================+
# |           Creates a csv file from previosuly generated csv files                     |
# +======================================================================================+
def csvWriter(input, output, date):
    with open(f"text/grouped_output/{input}_{date}.txt", "r") as f:
        with open(f"csv/{output}_{date}.csv", "w", newline="") as file:
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


def csvWriter2():
    input = "research"
    output = "research"
    date = "2023-08-10"
    with open(f"text/grouped_output/{input}_{date}.txt", "r") as f:
        with open(f"csv/{output}_{9999999}.csv", "w", newline="") as file:
            writer = csv.writer(file)
            if output == "research":
                headers = [
                    "Id",
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
            count = 1
            for line in f:
                trimmedWords = []
                line = line.split("|")
                trimmedWords.append(count)
                count = count + 1
                for word in line:
                    new_word = word.strip()
                    trimmedWords.append(new_word)
                # writer = csv.writer(file)
                writer.writerow(trimmedWords)


def csvChecker():
    print("hello")
