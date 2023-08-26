import sys
from pypdf import PdfReader
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tools
import writer
import time

# +======================================================================================+
# |           Official bar chart function that creates batches of user charts            |
# +======================================================================================+
def getUserBarChart(input, date):
    df = pd.read_csv(f"csv/{input}_{date}.csv")
    dfBase = pd.read_csv(f"csv/{input}_{date}.csv")

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
        divisor = tools.getDivisor(dfBase.iloc[i]["Tot.Used Space"])
        print(f"divsior: {divisor}")
        counter = tools.getChartCounter(divisor)
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
                color="tab:blue",
                label="AFS Group",
            )
            ax.bar_label(p1, label_type="center")

        if df.iloc[i]["Users AFS"] != 0:
            p2 = ax.bar(
                df.iloc[i]["Full Name"],
                df.iloc[i]["Users AFS"],
                width=0.5,
                color="tab:green",
                bottom=df.iloc[i]["AFS Groups"],
                label="AFS User",
            )
            ax.bar_label(p2, label_type="center")

        if df.iloc[i]["Users Panas."] != 0:
            p3 = ax.bar(
                df.iloc[i]["Full Name"],
                df.iloc[i]["Users Panas."],
                width=0.5,
                color="orange",
                bottom=df.iloc[i]["AFS Groups"] + df.iloc[i]["Users AFS"],
                label="Panasas User",
            )
            ax.bar_label(p3, label_type="center")

        ax.set(
            ylabel=counter, title=f"{df.iloc[i]['Full Name']}'s Storage Amounts {date}"
        )

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
            f"graphs/research/users/{df.iloc[i]['Full Name']}_user_report_{date}.pdf",
            dpi=300,
            format="pdf",
            bbox_extra_artists=(lgd,),
            bbox_inches="tight",
        )
        plt.close(fig)

# +======================================================================================+
# |           Official bar chart function that creates batches of user charts            |
# +======================================================================================+
def testBatchGetUserBarChart(input, date):
    start = time.time()
    df = pd.read_csv(f"csv/{input}_{date}.csv")

    # Calculating how many rows are in the datframe column "Full Name" *can make this a seperate function, may come in handy later*
    users = []
    for i in df["Full Name"]:
        users.append(i)
    length = len(users)

    for i in range(len(users)):
        # displaying debugging info
        print(f"User Index: {i}")
        print(f'Name {df.iloc[i]["Full Name"]}')
        print(f'Amount {df.iloc[i]["Tot.Used Space"]}')
        divisor = tools.getDivisor(df.iloc[i]["Tot.Used Space"])
        print(f"divsior: {divisor}")
        counter = tools.getChartCounter(divisor)
        print(f"counter: {counter}")

        
        df["AFS Groups"].iloc[i] = df.iloc[i]["AFS Groups"]/divisor
        df["Users AFS"].iloc[i] = df.iloc[i]["Users AFS"]/divisor
        df["Users Panas."].iloc[i] = df.iloc[i]["Users Panas."]/divisor
        df["Tot.Used Space"].iloc[i] = df.iloc[i]["Tot.Used Space"]/divisor

    print(df)
    # Generating a chart for each user found in "users" array
    for i in range(length):
        print(f"User Index: {i}")
        print(f'Name {df.iloc[i]["Full Name"]}')
        print(f'Amount {df.iloc[i]["Tot.Used Space"]}')
        divisor = tools.getDivisor(df.iloc[i]["Tot.Used Space"])
        print(f"divsior: {divisor}")
        counter = tools.getChartCounter(divisor)
        print(f"counter: {counter}")
        fig, ax = plt.subplots()

    
        if df.iloc[i]["AFS Groups"] != 0:
            p1 = ax.bar(
                df.iloc[i]["Full Name"],
                df.iloc[i]["AFS Groups"],
                width=0.5,
                color="tab:blue",
                label="AFS Group",
            )
            ax.bar_label(p1, label_type="center")

        if df.iloc[i]["Users AFS"] != 0:
            p2 = ax.bar(
                df.iloc[i]["Full Name"],
                df.iloc[i]["Users AFS"],
                width=0.5,
                color="tab:green",
                bottom=df.iloc[i]["AFS Groups"],
                label="AFS User",
            )
            ax.bar_label(p2, label_type="center")

        if df.iloc[i]["Users Panas."] != 0:
            p3 = ax.bar(
                df.iloc[i]["Full Name"],
                df.iloc[i]["Users Panas."],
                width=0.5,
                color="orange",
                bottom=df.iloc[i]["AFS Groups"] + df.iloc[i]["Users AFS"],
                label="Panasas User",
            )
            ax.bar_label(p3, label_type="center")

        ax.set(
            ylabel=counter, title=f"{df.iloc[i]['Full Name']}'s Storage Amounts {date}"
        )

        # Setting axis limits
        xlimits = ax.get_xlim()
        ax.set_xlim(left=-0.7, right=0.7)
        ylimits = ax.get_ylim()
        ax.set_ylim(bottom=None, top=(ylimits[1] + ylimits[1] * 0.15))

        # Displaying total on top of bar
        # total = np.float64(np.format_float_positional(total, precision=4))
        # ax.text(
        #     0,
        #     total + (total * 0.07),
        #     f"Total: {total}",
        #     ha="center",
        #     weight="bold",
        #     color="black",
        # )

        # Displaying legend
        lgd = ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

        # Saving the figure
        plt.savefig(
            f"graphs/research/tests/{df.iloc[i]['Full Name']}_user_report_{date}.pdf",
            dpi=300,
            format="pdf",
            bbox_extra_artists=(lgd,),
            bbox_inches="tight",
        )
        plt.close(fig)
    end = time.time()
    print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

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

    divisor = tools.getDivisor(df.iloc[i]["Tot.Used Space"])
    print(f'raw storage amount: {df.iloc[i]["Tot.Used Space"]}')
    print(f"divisor: {divisor}")
    counter = tools.getChartCounter(divisor)
    unit = tools.getUnit(counter)

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
