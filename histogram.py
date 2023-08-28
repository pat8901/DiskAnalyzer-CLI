import sys
from pypdf import PdfReader
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
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
    scott_bins = [0, 0.0005, 0.001, 0.1, 0.5, 1, 2, 10, 20, 50, 10000000]
    scott_labels = [
        "0GB-0.5GB",
        "0.5GB-1GB",
        "1GB-100GB",
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
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        print(df)

    # Setting the graph's x/y labels and title
    ax.set(
        ylabel="Frequency",
        title=f"{column} - Number of Users Within a Range of Storage {date}",
    )
    # ax.set_ylim([0, 50])

    # Creating bar plots and adding them to graph
    # for i in range(len(data)):
    #     p = ax.bar(better_bins_labels[i], data[i], label=better_bins_labels[i], width=1)
    #     ax.bar_label(p, label_type="edge")

    # Creating bar plots and adding them to graph
    for i in range(len(data)):
        if i == 0:
            continue
        if i == 1:
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
        f"graphs/research/group/test5_histogram_{group}_{column}_{date}.pdf",
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
    scott_bins = [0.001, 0.1, 0.5, 1, 2, 10, 20, 50, 10000000]
    scott_labels = [
        "1GB-100GB",
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
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        print(df)

    # Setting the graph's x/y labels and title
    ax.set(
        ylabel="Frequency",
        title=f"{column} - Number of Users Within a Range of Storage {date}",
    )
    # ax.set_ylim([0, 50])

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
        f"graphs/research/group/test2_histogram_{group}_{column}_{date}.pdf",
        dpi=300,
        format="pdf",
        # bbox_extra_artists=(lgd,),
        bbox_inches="tight",
    )

    plt.show()
