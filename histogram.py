import sys
from pypdf import PdfReader
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# import scipy.stats as stats
import tools
import writer
import bar
import pie
import misc


# +======================================================================================+
# |  Creates a histogram using binned data as x values and their frequencies as y values |
# |   *This is different from piechart as it would make sense to have 0 counts for bins* |
# +======================================================================================+
def getGroupHistogram(group, column, date):
    df = pd.read_csv(f"csv/{group}_{date}.csv")
    terabyte = 1000000000
    scott_bins = [0, 0.1, 0.5, 1, 2, 10, 20, 50, 10000000]
    scott_labels = [
        "0GB-100GB",
        "100GB-500GB",
        "500GB-1TB",
        "1TB-2TB",
        "2TB-10TB",
        "10TB-20TB",
        "20TB-50TB",
        "50TB-?TB",
    ]

    better_bins = tools.binCreator(80, 2, 0)
    better_bins_labels = tools.binLabelCreator(80, 2, 0)
    fig, ax = plt.subplots()

    # Covert data in column from kilobytes to terabytes
    df[f"{column}"] = df[f"{column}"].div(terabyte)

    # Creates a new column in dataframe with each row having their appropriate bin
    # df["bin"] = pd.cut(
    #     df[f"{column}"], better_bins, labels=better_bins_labels, right=False
    # )

    df["bin"] = pd.cut(df[f"{column}"], scott_bins, labels=scott_labels, right=False)

    # Counts the frequency of counts within bin ranges
    data = df["bin"].value_counts(sort=False)
    print(data)

    # *Debugging* Shows full table data
    # with pd.option_context("display.max_rows", None, "display.max_columns", None):
    #     print(df)

    # Setting the graph's x/y labels and title
    ax.set(
        ylabel="Frequency",
        title=f"{column} - Number of Users Within a Range of Storage {date}",
    )
    ax.set_ylim([0, 50])

    # Creating bar plots and adding them to graph
    # for i in range(len(data)):
    #     p = ax.bar(better_bins_labels[i], data[i], label=better_bins_labels[i], width=1)
    #     ax.bar_label(p, label_type="edge")

    # Creating bar plots and adding them to graph
    for i in range(len(data)):
        if i == 1:
            continue
        if i == 3:
            continue
        if i == 5:
            continue
        else:
            p = ax.bar(scott_labels[i], data[i], label=scott_labels[i], width=1)
            ax.bar_label(p, label_type="edge")

    # Legend - Not really needed
    # lgd = ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

    # Rotating x labels 90 degrees
    # plt.xticks(rotation=90, ha="right")
    plt.xticks(rotation=0, ha="center")

    # Setting the size of the graph for when it will be saved to a file
    figure = plt.gcf()
    figure.set_size_inches(24, 8.5)

    # Saving the figure
    plt.savefig(
        f"graphs/research/group/test1_histogram_{group}_{column}_{date}.pdf",
        dpi=300,
        format="pdf",
        # bbox_extra_artists=(lgd,),
        bbox_inches="tight",
    )

    # plt.show()


# +======================================================================================+
# |  Creates a histogram using binned data as x values and their frequencies as y values |
# |             *bins are auto-made using the hist function instead of bar*              |
# +======================================================================================+
def getBatchGroupHistogram(group, column, date):
    df = pd.read_csv(f"csv/{group}_{date}.csv")
    terabyte = 1000000000
    scott_bins = [0, 0.001, 0.1, 0.5, 1, 4, 10, 20, 50, 10000000]
    scott_labels = [
        "0GB-1GB",
        "1GB-100GB",
        "100GB-500GB",
        "500GB-1TB",
        "1TB-4TB",
        "4TB-10TB",
        "10TB-20TB",
        "20TB-50TB",
        "50TB-?TB",
    ]

    better_bins = tools.binCreator(80, 2, 0)
    better_bins_labels = tools.binLabelCreator(80, 2, 0)
    fig, ax = plt.subplots()

    # Covert data in column from kilobytes to terabytes
    df[f"{column}"] = df[f"{column}"].div(terabyte)

    # Creates a new column in dataframe with each row having their appropriate bin
    # df["bin"] = pd.cut(
    #     df[f"{column}"], better_bins, labels=better_bins_labels, right=False
    # )

    df["bin"] = pd.cut(df[f"{column}"], scott_bins, labels=scott_labels, right=False)

    # Counts the frequency of counts within bin ranges
    data = df["bin"].value_counts(sort=False)
    print(data)

    # *Debugging* Shows full table data
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        print(df)

    # Setting the graph's x/y labels and title
    ax.set_ylabel("Number of Users", fontsize=16)
    if column == "Tot.Used Space":
        ax.set_title(f"Total Used Space ({date})", fontsize=16)
    else:
        ax.set_title(f"{column} ({date})", fontsize=16)
    matplotlib.pyplot.xticks(fontsize=12)
    matplotlib.pyplot.yticks(fontsize=14)
    plt.figtext(
        0.12,
        0.01,
        f"*{data[0]} users between 0GB-1GB not displayed",
        horizontalalignment="left",
        fontsize=12,
    )
    # ax.grid(axis='y')

    # Creating bar plots and adding them to graph
    # for i in range(len(data)):
    #     p = ax.bar(better_bins_labels[i], data[i], label=better_bins_lab1els[i], width=1)
    #     ax.bar_label(p, label_type="edge")

    # Creating bar plots and adding them to graph
    for i in range(len(data)):
        if i == 0:
            continue
        else:
            p = ax.bar(
                scott_labels[i],
                data[i],
                label=scott_labels[i],
                width=1,
                edgecolor="white",
            )

            ax.bar_label(p, label_type="edge", fontsize=16)

    # Legend - Not really needed
    # lgd = ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

    # Rotating x labels 90 degrees
    # plt.xticks(rotation=90, ha="right")
    plt.xticks(rotation=0, ha="center")

    # Setting the size of the graph for when it will be saved to a file
    figure = plt.gcf()
    figure.set_size_inches(24, 8.5)

    # Saving the figure
    plt.savefig(
        f"graphs/research/group/{group}_{column}_histogram_{date}.pdf",
        dpi=300,
        format="pdf",
        # bbox_extra_artists=(lgd,),
        bbox_inches="tight",
    )

    plt.show()


# +======================================================================================+
# |  Creates a histogram using binned data as x values and their frequencies as y values |
# |             *bins are auto-made using the hist function instead of bar*              |
# +======================================================================================+
def getStackedGroupHistogram(group, date):
    df = pd.read_csv(f"csv/{group}_{date}.csv")
    terabyte = 1000000000
    colors = [
        "tab:blue",
        "tab:orange",
        "tab:green",
        "tab:purple",
        "tab:pink",
        "tab:cyan",
        "tab:gray",
        "tab:brown",
    ]
    better_bins = tools.binCreator(80, 2, 0)
    better_bins_labels = tools.binLabelCreator(80, 2, 0)
    scott_unused_bins = [0, 0.001]
    scott_unused_labels = ["0GB-1GB"]
    scott_bins = [0, 0.001, 0.1, 0.5, 1, 2, 10, 20, 50, 10000000]
    scott_labels = [
        "0GB-1GB",
        "1GB-100GB",
        "100GB-500GB",
        "500GB-1TB",
        "1TB-2TB",
        "2TB-10TB",
        "10TB-20TB",
        "20TB-50TB",
        "50TB-?TB",
    ]

    fig, ax = plt.subplots()

    # Covert data in column from kilobytes to terabytes
    df["AFS Groups"] = df["AFS Groups"].div(terabyte)
    df["Users AFS"] = df["Users AFS"].div(terabyte)
    df["Users Panas."] = df["Users Panas."].div(terabyte)
    df["Tot.Used Space"] = df["Tot.Used Space"].div(terabyte)

    # Creates a new column in dataframe with each row having their appropriate bin
    # df["bin"] = pd.cut(
    #     df[f"{column}"], better_bins, labels=better_bins_labels, right=False
    # )

    df["bin_AFS_Groups"] = pd.cut(
        df["AFS Groups"], scott_bins, labels=scott_labels, right=False
    )
    df["bin_Users_AFS"] = pd.cut(
        df["Users AFS"], scott_bins, labels=scott_labels, right=False
    )
    df["bin_Users_Panas."] = pd.cut(
        df["Users Panas."], scott_bins, labels=scott_labels, right=False
    )
    df["bin_total"] = pd.cut(
        df["Tot.Used Space"], scott_bins, labels=scott_labels, right=False
    )

    # Test bins to see if I can store a seperate copy of bin data from 0-1GB
    df["bin_AFS_Groups_unused"] = pd.cut(
        df["AFS Groups"], scott_unused_bins, labels=scott_unused_labels, right=False
    )
    df["bin_Users_AFS_unused"] = pd.cut(
        df["Users AFS"], scott_unused_bins, labels=scott_unused_labels, right=False
    )
    df["bin_Users_Panas._unused"] = pd.cut(
        df["Users Panas."], scott_unused_bins, labels=scott_unused_labels, right=False
    )
    df["bin_total_unused"] = pd.cut(
        df["Tot.Used Space"], scott_unused_bins, labels=scott_unused_labels, right=False
    )

    # Counts the frequency of counts within bin ranges
    data_AFS_Groups = df["bin_AFS_Groups"].value_counts(sort=False)
    data_Users_AFS = df["bin_Users_AFS"].value_counts(sort=False)
    data_Users_Panas = df["bin_Users_Panas."].value_counts(sort=False)
    data_total = df["bin_total"].value_counts(sort=False)

    data_AFS_Groups_unused = df["bin_AFS_Groups_unused"].value_counts(sort=False)
    data_Users_AFS_unused = df["bin_Users_AFS_unused"].value_counts(sort=False)
    data_Users_Panas_unused = df["bin_Users_Panas._unused"].value_counts(sort=False)
    data_total_unused = df["bin_total_unused"].value_counts(sort=False)

    # *Debugging* Shows full table data
    # with pd.option_context("display.max_rows", None, "display.max_columns", None):
    #     print(df)

    # Setting the graph's x/y labels and title
    ax.set(
        ylabel="Number of Users",
        title=f"Number of Users Within a Range of Storage {date}",
    )

    # Creating bar plots and adding them to graph
    # for i in range(len(data)):
    #     p = ax.bar(better_bins_labels[i], data[i], label=better_bins_labels[i], width=1)
    #     ax.bar_label(p, label_type="edge")

    # Creating bar plots and adding them to graph
    for i in range(len(data_AFS_Groups)):
        if i != 0:
            if data_AFS_Groups[i] != 0:
                p0 = ax.bar(
                    scott_labels[i], data_AFS_Groups[i], label=scott_labels[i], width=1
                )
                ax.bar_label(p0, label_type="center")
            if data_Users_AFS[i] != 0:
                p1 = ax.bar(
                    scott_labels[i],
                    data_Users_AFS[i],
                    label=scott_labels[i],
                    width=1,
                    bottom=data_AFS_Groups[i],
                )
                ax.bar_label(p1, label_type="center")
            if data_Users_Panas[i] != 0:
                p2 = ax.bar(
                    scott_labels[i],
                    data_Users_Panas[i],
                    label=scott_labels[i],
                    width=1,
                    bottom=data_AFS_Groups[i] + data_Users_AFS[i],
                )
                ax.bar_label(p2, label_type="center")
        else:
            continue

    # Legend - Not really needed
    lgd = ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.figtext(
        0.12,
        0.01,
        f"*{data_AFS_Groups[0]+data_Users_AFS[0]+data_Users_Panas[0]} users counts between 0GB-1GB not displayed    * unused count: {data_AFS_Groups_unused[0]+data_Users_AFS_unused[0]+data_Users_Panas_unused[0]}",
        horizontalalignment="left",
        fontsize=12,
    )

    # Rotating x labels 90 degrees
    # plt.xticks(rotation=90, ha="right")
    plt.xticks(rotation=0, ha="center")

    # Setting the size of the graph for when it will be saved to a file
    figure = plt.gcf()
    figure.set_size_inches(24, 8.5)

    # Saving the figure
    plt.savefig(
        f"graphs/research/group/stackTest_histogram_{group}_{date}.pdf",
        dpi=300,
        format="pdf",
        # bbox_extra_artists=(lgd,),
        bbox_inches="tight",
    )

    plt.show()
