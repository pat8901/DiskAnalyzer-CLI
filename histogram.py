import sys
from pypdf import PdfReader
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tools
import writer
import bar
import pie
import misc


# +======================================================================================+
# |  Creates a histogram using binned data as x values and their frequencies as y values |
# |   *This is different from piechart as it would make sense to have 0 counts for bins* |
# +======================================================================================+
def getGroupHistogram(input, column, date):
    df = pd.read_csv(f"csv/{input}_{date}.csv")
    terabyte = 1000000000
    xaxis = 0

    scott_bins = [0, 0.1, 0.5, 1, 2, 10, 20, 50, 10000000]
    scott_labels = [
        "0-100GB",
        "100-500GB",
        "500GB-1TB",
        "1-2TB",
        "2-10TB",
        "10-20TB",
        "20-50TB",
        "50-?TB",
    ]

    bin0 = [0, 0.1]
    label0 = ["0-100GB"]
    bin1 = [0.5, 1]
    label1 = ["500GB-1TB"]
    bin2 = [2, 10]
    label2 = ["2-10TB"]
    bin3 = [20, 50, 10000000]
    label3 = ["20-50TB", "50-?TB"]

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

    df["bin0"] = pd.cut(df[f"{column}"], bin0, labels=label0, right=False)
    df["bin1"] = pd.cut(df[f"{column}"], bin1, labels=label1, right=False)
    df["bin2"] = pd.cut(df[f"{column}"], bin2, labels=label2, right=False)
    df["bin3"] = pd.cut(df[f"{column}"], bin3, labels=label3, right=False)

    # Counts the frequency of counts within bin ranges
    data = df["bin"].value_counts(sort=False)
    data0 = df["bin0"].value_counts(sort=False)
    data1 = df["bin1"].value_counts(sort=False)
    data2 = df["bin2"].value_counts(sort=False)
    data3 = df["bin3"].value_counts(sort=False)
    print(data0)
    print(data1)
    print(data2)
    print(data3)
    print(data)
    # with pd.option_context("display.max_rows", None, "display.max_columns", 10):
    #     print(df)

    # *Debugging* Shows full table data
    # with pd.option_context("display.max_rows", None, "display.max_columns", None):
    #     print(data)

    # Setting the graph's x/y labels and title
    ax.set(
        ylabel="Frequency",
        title=f"{column} - Number of Users Within a Range of Storage {date}",
    )

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

    # p0 = ax.bar(label0, data0, label=label0, width=1)
    # ax.bar_label(p0, label_type="edge")
    # p1 = ax.bar(label1, data1, label=label1, width=1)
    # ax.bar_label(p1, label_type="edge")
    # p2 = ax.bar(label2, data2, label=label2, width=1)
    # ax.bar_label(p2, label_type="edge")
    # p3 = ax.bar(label3, data3, label=label3, width=1)
    # ax.bar_label(p3, label_type="edge")

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
        f"graphs/research/group/test_histogram_{column}_{date}.pdf",
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
def autoGetGroupHistogram(input, column):
    df = pd.read_csv(f"csv/{input}.csv")
    terabyte = 1000000000

    df[f"{column}"] = df[f"{column}"].div(terabyte)

    fig, ax = plt.subplots()
    ax.set(
        title=f"{input} {column} Storage in Terabytes",
    )
    ax.hist(df, [0, 1, 50, 100, 200, 300, 400, 500, 600])
    plt.show()
