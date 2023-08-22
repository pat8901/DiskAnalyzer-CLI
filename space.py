import sys
from pypdf import PdfReader
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def main():
    # input = sys.argv[1]
    # print(f'You said "{input}"')

    createFullOutput("Storage_Rep_2023-08-10.pdf")
    createResearchOutput()
    createDepartmentOutput()
    createCollegesOutput()

    csvWriter("research", "research")
    csvWriter("departments", "departments")
    csvWriter("colleges", "colleges")

    # How do I get rid of the bins with 0's so they dont display in the plots?
    # getGroupPieChart("research", "AFS Groups")
    # getGroupPieChart("colleges", "AFS Groups")

    getUserBarChart("research")


# +======================================================================================+
# |           Converts input pdf into a txt file to be used in further processing        |
# |                           *Can be optimized further*                                 |
# +======================================================================================+
def createFullOutput(input):
    pdf = open(f"{input}", "rb")
    reader = PdfReader(pdf)
    with open("tmp/full_output.txt", "w") as f_output:
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


# +======================================================================================+
# |           Converts input pdf into a txt file to be used in further processing        |
# |                           *Can be optimized further*                                 |
# +======================================================================================+
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


# +======================================================================================+
# |           Converts input pdf into a txt file to be used in further processing        |
# |                           *Can be optimized further*                                 |
# +======================================================================================+
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


# +======================================================================================+
# |           Converts input pdf into a txt file to be used in further processing        |
# |                           *Can be optimized further*                                 |
# +======================================================================================+
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
# |             This fucntion may be helpful in adding labels to graphs                  |
# +======================================================================================+
def testPlot():
    df = pd.read_csv("csv/research.csv")
    # df.plot()
    # plt.show()

    df["Tot.Used Space"].plot(
        kind="bar",
        x="Full Name",
        y="Tot.Used Space",
    )
    plt.show()
    print(df)


# +======================================================================================+
# |             Creates a stacked bar chart displaying the different amounts             |
# |                           of storage a user is using                                 |
# +======================================================================================+
def getUserBarChart(input):
    terabyte = 1000000000
    df = pd.read_csv(f"csv/{input}.csv")
    users = []
    for i in df["Full Name"]:
        users.append(i)
    length = len(users)

    df["AFS Groups"] = df["AFS Groups"].div(terabyte)

    # May be able to use in your pie chart issue to filter out the zeros ex. df.loc[df["Full Name"] != "Patrick Joseph Flynn"]
    print(df.loc[df["Full Name"] == "Patrick Joseph Flynn"])
    for i in range(length):
        print(i)
        fig, ax = plt.subplots()
        ax.bar(df.iloc[i]["Full Name"], df.iloc[i]["AFS Groups"], width=0.5)
        ax.set(
            ylabel="Terabytes",
            xlabel="User",
            title=f"{df.iloc[i]['Full Name']}'s AFS Storage Amount",
        )
        plt.savefig(f"graphs/research/user/{df.iloc[i]['Full Name']}_user_report.pdf")
        plt.close(fig)
        # plt.show()

    # for i in users:
    #     print(df.loc[df["Full Name"] == f"{i}"])
    #     p = ax.bar()
    #     fig, ax = plt.subplots()
    #     x = i
    #     y1 = df["AFS Groups"]
    #     y2 = "Users AFS"
    #     y3 = "Users Panas."
    #     y4 = "Tot.Used Space"
    #     ax.set(
    #         title=f"User Storage's in Terabytes",
    #     )
    #     ax.bar(x, y1)
    #     ax.bar(x, y2, bottom=y1)
    #     ax.bar(x, y3, bottom=y1 + y2)
    #     ax.bar(x, y4, bottom=y1 + y2 + y3)
    #     plt.show()


# +======================================================================================+
# | This function takes in a csv file and a single column which then creates a pie chart |
# | displaying the counts of binned data within a specified range                        |
# +======================================================================================+
def getGroupPieChart(input, column):
    terabyte = 1000000000
    bins = [0, 1, 50, 100, 200, 300, 400, 500, 600]
    labels = [
        "0-1 TB",
        "1-50 TB",
        "50-100 TB",
        "100-200 TB",
        "200-300 TB",
        "300-400 TB",
        "400-500 TB",
        "500 TB >",
    ]
    df = pd.read_csv(f"csv/{input}.csv")

    df[f"{column}"] = df[f"{column}"].div(terabyte)
    df = df.sort_values(f"{column}", ascending=False)
    df["bin"] = pd.cut(
        df[f"{column}"],
        bins,
        labels=labels,
    )

    data = df["bin"].value_counts()
    id = df["bin"]

    fig, ax = plt.subplots()
    ax.set(
        title=f"{input} {column} Storage in Terabytes",
    )
    ax.pie(
        data,
        labels=labels,
        autopct="%1.1f%%",
    )
    plt.show()


# +======================================================================================+
# |         This function creates a plot for a individual displaying storages            |
# |                             *Not Complete*                                           |
# +======================================================================================+
def testCollegeIndividualPlot():
    terabyte = 1000000000
    df = pd.read_csv("csv/colleges.csv")
    df["Tot.Used Space"] = df["Tot.Used Space"].div(terabyte)
    storage = {"afs": df["AFS Groups"], "total": df["Tot.Used Space"]}

    fig, ax = plt.subplots()

    for i, storage in storage.items():
        p = ax.bar(
            storage,
            height=500,
            label=i,
        )

    ax.bar_label(p, label_type="center")

    # ax.set_title('')
    ax.legend()

    plt.show()


# +======================================================================================+
# |             This fucntion may be helpful in adding labels to graphs                  |
# +======================================================================================+
def testCollegeGroupPlot():
    terabyte = 1000000000

    df = pd.read_csv("csv/colleges.csv")
    df = df.sort_values("Tot.Used Space", ascending=False)
    print(df)
    df["Tot.Used Space"] = df["Tot.Used Space"].div(terabyte)
    print("=========================================================")
    print(df)
    x = df["College Name"]
    y = df["Tot.Used Space"]
    # y = np.arange(0, 17)
    fig, ax = plt.subplots()

    # addlabels(x, y)

    ax.bar(
        x,
        y,
        width=1,
        edgecolor="white",
        color="purple",
        linewidth=0.7,
    )

    ax.set(
        ylabel="Terabytes",
        xlabel="Colleges",
        title="Total College Storage",
        # xlim=(0, 19),
        # ylim=(0, 100000000000),
        # yticks=[0, 100, 100000, 100000000, 100000000000],
    )

    ax.grid(visible=True, axis="y")

    plt.xticks(rotation=45, ha="right")
    plt.savefig("graphs/colleges/college_group_test.png")
    plt.savefig("graphs/colleges/college_group_test.pdf")
    plt.show()


# +======================================================================================+
# |                 Frequency binning function to plot pie chart                         |
# +======================================================================================+
def frequencyPlot():
    data = pd.read_csv("csv/research.csv")
    df = data["Tot.Used Space"].value_counts(bins="3")
    print(df)


if __name__ == "__main__":
    main()
