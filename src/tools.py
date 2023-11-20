import sys
from pypdf import PdfReader
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# +======================================================================================+
# |       Tool to determine the proper divisor to use when given a pandas dataframe      |
# |             Uses the total storage of a user to calculate the divisor                |
# +======================================================================================+
def getDivisor(input):
    # may be faster to do bit shifting?
    terabyte = 1000000000
    gigabyte = 1000000
    megabyte = 1000
    kilobyte = 1

    if terabyte <= input:
        return terabyte
    elif gigabyte <= input < terabyte:
        return gigabyte
    elif megabyte <= input < gigabyte:
        return megabyte
    else:
        return kilobyte


# +======================================================================================+
# |       Tool to determine the proper divisor to use when given a pandas dataframe      |
# |             Uses the total storage of a user to calculate the divisor                |
# +======================================================================================+
def getDivisorArray(inputArray):
    # may be faster to do bit shifting?
    terabyte = 1000000000
    gigabyte = 1000000
    megabyte = 1000
    kilobyte = 1
    outputArray = np.zeros(len(inputArray))

    np.array(inputArray)
    for i in range(inputArray):
        if terabyte <= input:
            outputArray = np.insert(outputArray, i, terabyte)
        elif gigabyte <= input < terabyte:
            outputArray = np.insert(outputArray, i, gigabyte)
        elif megabyte <= input < gigabyte:
            outputArray = np.insert(outputArray, i, megabyte)
        else:
            outputArray = np.insert(outputArray, i, kilobyte)

    return outputArray


# +======================================================================================+
# |               Tool to number to its corresponding name returns a string              |
# +======================================================================================+
def getChartCounter(input):
    terabyte = 1000000000
    gigabyte = 1000000
    megabyte = 1000
    kilobyte = 1

    if input == terabyte:
        return "Terabytes"
    elif input == gigabyte:
        return "Gigabytes"
    elif input == megabyte:
        return "Megabytes"
    else:
        return "Kilobytes"


# +======================================================================================+
# |               Tool to number to its corresponding name returns a string              |
# +======================================================================================+
def getUnit(input):
    if input == "Terabytes":
        return "TB"
    elif input == "Gigabytes":
        return "GB"
    elif input == "Megabytes":
        return "MB"
    else:
        return "KB"


# +======================================================================================+
# |             This function sums the column of Total Storage and prints                |
# |                           onto the screen in terabytes                               |
# +======================================================================================+
def getTotalStorage():
    total = 0
    df = pd.read_csv("csv/research.csv")
    total = df["Tot.Used Space"].sum()
    terabyte = total / 1000000000
    print(f"Total Storage (KB): {total}")
    print(f"Total Storage (TB): {terabyte}")


# +======================================================================================+
# |             This fucntion may be helpful in adding labels to graphs                  |
# +======================================================================================+
def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])


# +======================================================================================+
# |             Creates a list of bin labels to be used with frequency graphs            |
# +======================================================================================+
def binLabelCreator(amount, step, start):
    bin_labels = []
    bin_labels.append(f"{start}-{step}")
    left = step
    for i in range(amount - 1):
        bin_labels.append(f"{left}-{left+step}")
        left = left + step
    return bin_labels


# +======================================================================================+
# |             Creates a list of bin to be used with frequency graphs                   |
# +======================================================================================+
def binCreator(amount, step, start):
    bins = []
    bins.append(start)
    left = step
    for i in range(amount):
        bins.append(left)
        left = left + step
    # bins.append()
    return bins


# +======================================================================================+
# |                       Reformates the date to American Standard                       |
# +======================================================================================+
def dateFormatter(date):
    print(date)


# +======================================================================================+
# |                       Fetches the date of the input report                           |
# +======================================================================================+
def getReportDate(report_file):
    return report_file[-14:-4]


# +======================================================================================+
# |                       Fetches the path of the input report                           |
# +======================================================================================+
def getFilePath(report_file):
    return report_file[-14:-4]


# +======================================================================================+
# |                       Fetches the file name of input report                           |
# +======================================================================================+
def getFileName(report_file):
    return report_file[-26:]


# +======================================================================================+
# |                Tool to choose what format you want to save figures in                |
# +======================================================================================+
def getFormat():
    print(f"you selected png")
