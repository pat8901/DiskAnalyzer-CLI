"""
Copyright (c) 2023 Patrick O'Brien-Seitz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import sys
from pypdf import PdfReader
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import click


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


def getMonth(date):
    # Extracting the month from the given date. Based on the month it will be changed from number format to words
    month = date[5:7]
    if month == "01":
        month = "January"
    if month == "02":
        month = "Feburary"
    if month == "03":
        month = "March"
    if month == "04":
        month = "April"
    if month == "05":
        month = "May"
    if month == "06":
        month = "June"
    if month == "07":
        month = "July"
    if month == "08":
        month = "August"
    if month == "09":
        month = "September"
    if month == "10":
        month = "October"
    if month == "11":
        month = "November"
    if month == "12":
        month = "December"
    return month


def sortUsers(group, year, month, date):
    """Read file containing user names, alphabetically sort them and return as a list"""
    with open(
        f"documents/text/names/{year}/{month}/{group}_{date}.txt", "r"
    ) as file_input:
        sorted_users = []
        for user in file_input:
            user = user.strip()
            sorted_users.append(user)  # Append the name to the list

    return sorted(sorted_users)


def searchUsers(sorted_users):
    """Searches alphabetically sorted list of users based on search input provided"""
    while True:
        found_users = []
        found = False
        count = 1
        search_input = input("Enter user to search:").lower()
        print("============================")
        for user in sorted_users:
            if search_input in user.lower():
                print(f"{count}: {user}")
                found_users.append(user)
                count += 1
        print("============================\n")
        # if len(found_users) == 1:
        #     print(f"found user: {found_users[0]}")
        #     return found_users[0]
        return found_users


def selectUser(found_users):
    length = len(found_users)
    while True:
        user_input = input("Select User's Number or Type 's' to search again: ")
        if int(user_input) > length:
            click.echo(click.style("Enter a Valid Number!", fg="red"))
            continue
        user = found_users[int(user_input) - 1]
        response = click.confirm(f"Create a Graph For {user}?", abort=False)
        if response == True:
            return user
        else:
            return False
