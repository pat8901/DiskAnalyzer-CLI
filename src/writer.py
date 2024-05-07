"""
Copyright (c) 2024 Patrick O'Brien-Seitz

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

import os
from pypdf import PdfReader
import csv
import src.tools


def createFullOutput(input, date):
    """Can be optimized further.
    Converts input pdf into a txt file to be used in further processing.
    """
    
    pdf = open(f"{input}", "rb")
    reader = PdfReader(pdf)

    with open(f"./documents/text/full_output/full_output_{date}.txt", "w") as f_output:
        count = 0
        # Loop through each page
        for i in reader.pages:
            # Set "page" variable to the current page on loop
            page = reader.pages[count]
            text = page.extract_text()  # Extract the text from the pdf page
            f_output.write(text + "\n")  # Append to the opened writting file
            count += 1  # Do I even need to count like this?


def createResearchOutput(date):
    """ Takes full text file and splits into information only containing researchers. This txt file will be used in further processing.   
    *Can be optimized further, can probably combine with others* 
    """
    
    # This is where the research information begin
    begin = "-------------------------------   -------    ------------    ------------    ------------    --------------"
    # This is where the research information ends
    end = "=========================================|===============|===============|===============|=================|"
    beginFound = False  # Flag to know if the beginning was found

    # Checking to see if the "year" directory exist for the following path
    research_save_path = f"./documents/text/grouped_output/research"
    research_is_exist = os.path.exists(research_save_path)
    # If the path does not exist then make it
    if not research_is_exist:
        os.makedirs(research_save_path)  # Creating the directory
        print(f"Directory {research_save_path} was created!")

    # Reads full text file which contatins information on all groups
    with open(f"./documents/text/full_output/full_output_{date}.txt", "r") as f_input:
        # Open a file to be written to in the end will only contain information on researchers
        with open(
            f"./documents/text/grouped_output/research/research_{date}.txt", "w"
        ) as f_output:
            # Loop through each line in input file
            for line in f_input:
                # If the "end" string is found then you must have reach the end so break
                if end in line:
                    break
                # If the beginFound flag was found then you must be at the beginning so start writting to file
                if beginFound:
                    line = line.strip()  # Strip excess white space off of the line
                    line = line[:-1]  # *WHAT?*
                    f_output.write(line + "\n")  # Write to file output
                # If the "begin" string is in the line then set the beginfound flag to True
                elif begin in line:
                    beginFound = True


def createDepartmentOutput(date):
    """ 
    Takes full text file and splits into information only containing departments. This txt file will be used in further processing.
    *Can be optimized further, can probably combine with others*
    """
    
    header = "                                            Space Used by Departments"
    # This is where the departments information begins
    begin = "-----------------------------------------    ------------    ------------    ------------    --------------"
    # This is where the departments information ends
    end = "=========================================|===============|===============|===============|=================|"
    headerFound = False  # Flasg to know if the header was found
    beginFound = False  # Flag to know if the beginning was found

    # Checking to see if the "year" directory exist for the following path
    department_save_path = f"./documents/text/grouped_output/departments"
    department_is_exist = os.path.exists(department_save_path)
    # If the path does not exist then make it
    if not department_is_exist:
        os.makedirs(department_save_path)  # Creating the directory
        print(f"Directory {department_save_path} was created!")

    # Read the full text file
    with open(f"./documents/text/full_output/full_output_{date}.txt", "r") as f_input:
        # Open a new file to write department information to
        with open(
            f"./documents/text/grouped_output/departments/departments_{date}.txt", "w"
        ) as f_output:
            for line in f_input:  # Loop through each line in the file input
                # If the header is in the current line set "headerFound" to True
                if header in line:
                    headerFound = True
                # Run the code below only when the header is found
                if headerFound:
                    # If the "end" string is in the current line stop the loop
                    if end in line:
                        break
                    elif beginFound:  # If the beginning was found then process the line
                        line = line.strip()  # Strip excess whitespace of the line
                        line = line[:-1]  # *WHAT?*
                        f_output.write(line + "\n")  # Write the line to the output file
                    # If beginning is in the current line then set the flag to True
                    elif begin in line:
                        beginFound = True


def createCollegesOutput(date):
    """ 
    Takes full text file and splits into information only containing colleges. This txt file will be used in further processing.
    *Can be optimized further, can probably combine with others*
    """
    
    header = "                                            Space Used by Colleges"
    # This is where colleges information begins
    begin = "-----------------------------------------    ------------    ------------    ------------    --------------"
    # This is where colleges information ends
    end = "=========================================|===============|===============|===============|=================|"
    headerFound = False  # Flag to know if header was found
    beginFound = False  # Flag to know if the beginning was found

    # Checking to see if the "year" directory exist for the following path
    college_save_path = f"./documents/text/grouped_output/colleges"
    college_is_exist = os.path.exists(college_save_path)
    # If the path does not exist then make it
    if not college_is_exist:
        os.makedirs(college_save_path)  # Creating the directory
        print(f"Directory {college_save_path} was created!")

    # Reading the full text file
    with open(f"./documents/text/full_output/full_output_{date}.txt", "r") as f_input:
        # Opening a new file to write to
        with open(
            f"./documents/text/grouped_output/colleges/colleges_{date}.txt", "w"
        ) as f_output:
            # Looping through each line in the input file
            for line in f_input:
                # If the header is in the current line set it's flag to True
                if header in line:
                    headerFound = True
                # If header flag is True run the code below
                if headerFound:
                    # If "end" string is in the current line stop looping
                    if end in line:
                        break
                    # If the beginning flag is True run process the line
                    elif beginFound:
                        line = line.strip()  # Strip excess whitespace off of the line
                        line = line[:-1]  # *WHAT?*
                        f_output.write(line + "\n")  # Write the line to the output file
                    # If the "beginning" string is found in the current line then set it's flag to True
                    elif begin in line:
                        beginFound = True


def csvWriter(input, output, date):
    """Creates a csv file from previosuly generated text files."""
    
    # Replace _ with - for proper formatting
    folder_date = date.replace("-", "_")
    # Grab the year string
    folder_year = folder_date[0:-6]
    # Grab the month string
    month = folder_date[5:7]

    # Depending on what the month string it will be converted to words
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

    # Checking to see if the "year" directory exist for the following path
    year_save_path = f"./documents/csv/{folder_year}"
    year_is_exist = os.path.exists(year_save_path)
    # If the path does not exist then make it
    if not year_is_exist:
        os.makedirs(year_save_path)  # Creating the directory
        print(f"Directory {year_save_path} was created!")

    # Checking to see if the "month" directory exist for the following path
    save_path = f"./documents/csv/{folder_year}/{month}"
    is_exist = os.path.exists(save_path)
    # If the path does not exist then make it
    if not is_exist:
        os.makedirs(save_path)  # Creating the directory
        print(f"Directory {save_path} was created!")

    # Reading the corresponding grouped text files based on group and date given
    with open(f"./documents/text/grouped_output/{input}/{input}_{date}.txt", "r") as f:
        # Openning a new file to write csv data to
        with open(
            f"./documents/csv/{folder_year}/{month}/{output}_{date}.csv",
            "w",
            newline="",
        ) as file:
            # Creating a csv writer object *is this actually an object?*
            writer = csv.writer(file)
            # If output is research set these header parameters
            if output == "research":
                headers = [
                    "Full Name",
                    "DepCode",
                    "AFS Groups",
                    "Users AFS",
                    "Users Panas.",
                    "Tot.Used Space",
                ]
                # Write the parameters to the head of the csv file
                writer.writerow(headers)
            # If output is departments set these header parameters
            if output == "departments":
                headers = [
                    "Department",
                    "AFS Groups",
                    "Users AFS",
                    "Users Panas.",
                    "Tot.Used Space",
                ]
                # Write the parameters to the head of the csv file
                writer.writerow(headers)
            # If output is colleges set these header parameters
            if output == "colleges":
                headers = [
                    "College Name",
                    "AFS Groups",
                    "Users AFS",
                    "Users Panas.",
                    "Tot.Used Space",
                ]
                # Write the parameters to the head of the csv file
                writer.writerow(headers)
            # Loop through each line in the input file
            for line in f:
                trimmedWords = []  # A list to store words in a line
                line = line.split("|")  # Split the current line by "|"
                # Loop through each word in a line
                for word in line:
                    new_word = word.strip()  # Strip excess whitespace off each word
                    # Append the proccessed word to the "trimmedWords" list
                    trimmedWords.append(new_word)
                # Write the list of proccessed words to a row in the csv file
                writer.writerow(trimmedWords)


def csvWriter2():
    """*This is not used*
    Creates a csv file from previosuly generated text files.
    This is different from the other csv file writter as it also creates an ID row.
    The IDs are increments for each row loop.
    """
    
    input = "research"
    output = "research"
    date = "2023-08-10"
    with open(f"./documents/text/grouped_output/{input}_{date}.txt", "r") as f:
        with open(f"./documents/csv/{output}_{9999999}.csv", "w", newline="") as file:
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
            # Starting the ID count
            count = 1
            for line in f:
                trimmedWords = []
                line = line.split("|")
                trimmedWords.append(count)  # Append the ID number first
                count += 1  # Incrementing the count by one
                for word in line:
                    new_word = word.strip()
                    trimmedWords.append(new_word)
                writer.writerow(trimmedWords)


def nameExtractor():
    """Gets the names found in a group text file and returns an array of names."""
    
    groups = ["research", "colleges", "departments"]

    # Read a group text file
    with open(
        "./documents/text/grouped_output/research/research_2023-08-10.txt", "r"
    ) as file:
        names = []  # Store names in this list
        # Loop through each line in the input file
        for line in file:
            line = line.split("|")  # Split the line by "|"
            # Strip off excess whitespace for the first item in the line i.e. the name
            name = line[0].strip()
            names.append(name)  # Append the name to the list
    return names


def nameGenerator(date):
    """creates files of names for each report uploaded."""
    
    groups = ["research", "colleges", "departments"]
    # Replace _ with - for proper formatting
    # date = date.replace("-", "_")
    # month = date.replace("-", "_")
    month = src.tools.getMonth(date)
    year = date[0:-6]

    # Checking to see if the "year" directory exist, and creating it if not found
    year_save_path = f"./documents/text/names/{year}"
    year_is_exist = os.path.exists(year_save_path)
    if not year_is_exist:
        os.makedirs(year_save_path)
        print(f"Directory {year_save_path} was created!")
    # Checking to see if the "month" directory exist, and creating it if not found
    save_path = f"./documents/text/names/{year}/{month}"
    is_exist = os.path.exists(save_path)
    if not is_exist:
        os.makedirs(save_path)
        print(f"Directory {save_path} was created!")

    # Loop through each group to make name files for each
    for group in groups:
        # Reading the group text file for the currently selected group
        with open(
            f"./documents/text/grouped_output/{group}/{group}_{date}.txt", "r"
        ) as input_file:
            # Open a new file to write the names to
            with open(
                f"./documents/text/names/{year}/{month}/{group}_{date}.txt", "w"
            ) as output:
                for line in input_file:
                    line = line.split("|")
                    name = line[0].strip()
                    output.write(name + "\n")


def generateReports(input, date):
    """Calls all the functions to generate reports in one go."""
    
    groups = ["research", "colleges", "departments"]

    # Convert pdf to text file
    createFullOutput(input, date)
    createResearchOutput(date)
    createCollegesOutput(date)
    createDepartmentOutput(date)
    nameGenerator(date)

    # For each group takes it's corresponding text file and create a csv file from it
    for group in groups:
        csvWriter(group, group, date)
