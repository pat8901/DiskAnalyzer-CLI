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

    # getUserBarChart("research")
    # test_getUserBarChart("research")
    finaltestgetUserBarChart("research")


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
        ax.bar(df.iloc[i]["Full Name"], df.iloc[i]["Users AFS"], width=0.5)
        ax.set(
            ylabel="Terabytes",
            xlabel="User",
            title=f"{df.iloc[i]['Full Name']}'s AFS Storage Amount",
        )
        ax.legend(loc="upper right")
        plt.savefig(f"graphs/research/user/{df.iloc[i]['Full Name']}_user_report.pdf")
        plt.close(fig)
        # plt.show()


# +======================================================================================+
# |           Official bar chart function that creates batches of user charts            |
# +======================================================================================+
def finaltestgetUserBarChart(input):
    df = pd.read_csv(f"csv/{input}.csv")
    dfBase = pd.read_csv(f"csv/{input}.csv")

    # Calculating how many rows are in the datframe column "Full Name" *can make this a seperate function, may come in handy later*
    users = []
    for i in df["Full Name"]:
        users.append(i)
    length = len(users)

    afsGroups = np.array(df["AFS Groups"])
    afsUsers = np.array(df["Users AFS"])
    panasasUsers = np.array(df["Users Panas."])
    totalSpace = np.array(df["Tot.Used Space"])

    # Generating a chart for each user found in "users" array
    for i in range(length):
        print(f"User Index: {i}")
        print(f'Name {df.iloc[i]["Full Name"]}')
        print(f'Amount {df.iloc[i]["Tot.Used Space"]}')
        divisor = getDivisor(dfBase.iloc[i]["Tot.Used Space"])
        print(f"divsior: {divisor}")
        counter = getChartCounter(divisor)
        print(f"counter: {counter}")

        # dfTest["AFS Groups"] = df["AFS Groups"]
        # dfTest["Users AFS"] = df["Users AFS"]
        # dfTest["Users Panas."] = df["Users Panas."]
        # dfTest["Tot.Used Space"] = df["Tot.Used Space"]

        df["AFS Groups"] = dfBase["AFS Groups"].div(divisor)
        df["Users AFS"] = dfBase["Users AFS"].div(divisor)
        df["Users Panas."] = dfBase["Users Panas."].div(divisor)
        df["Tot.Used Space"] = dfBase["Tot.Used Space"].div(divisor)

        # Using numpy to create an array to house total values. May be better to use numpy to hold values of the other columns too!
        array = np.array(df["Tot.Used Space"])
        total = array[i]

        fig, ax = plt.subplots()

        if df.iloc[i]["AFS Groups"] != 0:
            p1 = ax.bar(
                df.iloc[i]["Full Name"],
                df.iloc[i]["AFS Groups"],
                width=0.5,
                color="lightblue",
                label="AFS Group",
            )
            ax.bar_label(p1, label_type="center")

        if df.iloc[i]["Users AFS"] != 0:
            p2 = ax.bar(
                df.iloc[i]["Full Name"],
                df.iloc[i]["Users AFS"],
                width=0.5,
                color="lightgreen",
                bottom=df.iloc[i]["AFS Groups"],
                label="AFS User",
            )
            ax.bar_label(p2, label_type="center")

        if df.iloc[i]["Users Panas."] != 0:
            p3 = ax.bar(
                df.iloc[i]["Full Name"],
                df.iloc[i]["Users Panas."],
                width=0.5,
                color="lightcoral",
                bottom=df.iloc[i]["AFS Groups"] + df.iloc[i]["Users AFS"],
                label="Panasas User",
            )
            ax.bar_label(p3, label_type="center")

        ax.set(ylabel=counter, title=f"{df.iloc[i]['Full Name']}'s Storage Amounts")

        # Setting axis limits
        xlimits = ax.get_xlim()
        ax.set_xlim(left=-0.7, right=0.7)
        ylimits = ax.get_ylim()
        ax.set_ylim(bottom=None, top=(ylimits[1] + ylimits[1] * 0.15))

        # Displaying total on top of bar
        total = np.float64(np.format_float_positional(total, precision=4))
        ax.text(
            0,
            total + (total * 0.07),
            f"Total: {total}",
            ha="center",
            weight="bold",
            color="black",
        )

        # Displaying legend
        lgd = ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

        # Saving the figure
        plt.savefig(
            f"graphs/research/users/{df.iloc[i]['Full Name']}_user_report.pdf",
            dpi=300,
            format="pdf",
            bbox_extra_artists=(lgd,),
            bbox_inches="tight",
        )
        plt.close(fig)


# +======================================================================================+
# |             Testing function for when getting a user's bar chart of storages         |
# |                         Only creates one user at a time                              |
# +======================================================================================+
def test_getUserBarChart(input):
    terabyte = 1000000000
    gigabyte = 1000000
    megabyte = 1000
    kilobytes = 1
    i = 112
    df = pd.read_csv(f"csv/{input}.csv")

    # May be able to use in your pie chart issue to filter out the zeros ex. df.loc[df["Full Name"] != "Patrick Joseph Flynn"]
    print(df.loc[df["Full Name"] == "Patrick Joseph Flynn"])

    divisor = getDivisor(df.iloc[i]["Tot.Used Space"])
    print(f'raw storage amount: {df.iloc[i]["Tot.Used Space"]}')
    print(f"divisor: {divisor}")
    counter = getChartCounter(divisor)
    unit = getUnit(counter)

    # Converting units
    df["AFS Groups"] = df["AFS Groups"].div(divisor)
    df["Users AFS"] = df["Users AFS"].div(divisor)
    df["Users Panas."] = df["Users Panas."].div(divisor)
    df["Tot.Used Space"] = df["Tot.Used Space"].div(divisor)

    # Using numpy to create an array to house total values. May be better to use numpy to hold values of the other columns too!
    array = np.array(df["Tot.Used Space"])
    total = array[i]

    print(f"User index: {i}")
    fig, ax = plt.subplots()
    if df.iloc[i]["AFS Groups"] != 0:
        p1 = ax.bar(
            df.iloc[i]["Full Name"],
            df.iloc[i]["AFS Groups"],
            width=0.5,
            color="lightblue",
            label="AFS Group",
        )
        ax.bar_label(p1, label_type="center")

    if df.iloc[i]["Users AFS"] != 0:
        p2 = ax.bar(
            df.iloc[i]["Full Name"],
            df.iloc[i]["Users AFS"],
            width=0.5,
            color="lightgreen",
            bottom=df.iloc[i]["AFS Groups"],
            label="AFS User",
        )
        ax.bar_label(p2, label_type="center")

    if df.iloc[i]["Users Panas."] != 0:
        p3 = ax.bar(
            df.iloc[i]["Full Name"],
            df.iloc[i]["Users Panas."],
            width=0.5,
            color="lightcoral",
            bottom=df.iloc[i]["AFS Groups"] + df.iloc[i]["Users AFS"],
            label="Panasas User",
        )
        ax.bar_label(p3, label_type="center")

    if df.iloc[i]["Tot.Used Space"] == 0:
        p4 = ax.bar(
            "Total Storage",
            df.iloc[i]["Tot.Used Space"],
            width=0.5,
            color="slateblue",
            label="Tot.Used Space",
        )
        ax.bar_label(
            # p4, labels=[f"{df.iloc[i]['Tot.Used Space']} {unit}"], label_type="center"
            p4,
            label_type="center",
        )

    ax.set(ylabel=counter, title=f"{df.iloc[i]['Full Name']}'s Storage Amounts")

    # Setting axis limits
    xlimits = ax.get_xlim()
    ax.set_xlim(left=-0.7, right=0.7)
    ylimits = ax.get_ylim()  # getting the current yaxis limits
    ax.set_ylim(bottom=None, top=(ylimits[1] + ylimits[1] * 0.15))

    # Displaying total on top of bar
    print(f"total value: {array[i]}")
    total = np.float64(np.format_float_positional(total, precision=4))
    print(total)
    ax.text(
        0,
        total + (total * 0.07),
        f"Total: {total}",
        ha="center",
        weight="bold",
        color="black",
    )

    # ax.ticklabel_format()
    # ax.legend([p1, p2, p3, p4], ["AFS Groups", "Users AFS", "Users Panas.", "Tot.Used Space"])
    lgd = ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

    # Saving the figure
    plt.savefig(
        f"graphs/research/tests/{df.iloc[i]['Full Name']}_user_report.pdf",
        dpi=300,
        format="pdf",
        bbox_extra_artists=(lgd,),
        bbox_inches="tight",
    )
    plt.show()


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
# |                 Frequency binning function to plot pie chart                         |
# +======================================================================================+
def frequencyPlot():
    data = pd.read_csv("csv/research.csv")
    df = data["Tot.Used Space"].value_counts(bins="3")
    print(df)


if __name__ == "__main__":
    main()
