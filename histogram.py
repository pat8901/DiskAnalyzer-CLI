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
    bins = [0, 1, 50, 100, 200, 300, 400, 500, 600]
    better_bins = tools.binCreator(80, 2, 0)
    better_bins_labels = tools.binLabelCreator(80, 2, 0)
    fig, ax = plt.subplots()

    # Covert data in column from kilobytes to terabytes
    df[f"{column}"] = df[f"{column}"].div(terabyte)

    # Creates a new column in dataframe with each row having their appropriate bin
    df["bin"] = pd.cut(
        df[f"{column}"], better_bins, labels=better_bins_labels, right=False
    )

    # Counts the frequency of counts within bin ranges
    data = df["bin"].value_counts(sort=False)

    # *Debugging* Shows full table data
    # with pd.option_context("display.max_rows", None, "display.max_columns", None):
    #     print(data)

    # Setting the graph's x/y labels and title
    ax.set(
        ylabel="Frequency",
        xlabel="Terabytes",
        title=f"{column} - Number of Users Within a Range of Storage {date}",
    )

    # Creating bar plots and adding them to graph
    for i in range(len(data)):
        p = ax.bar(better_bins_labels[i], data[i], label=better_bins_labels[i], width=1)
        ax.bar_label(p, label_type="edge")

    # Legend - Not really needed
    # lgd = ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

    # Rotating x labels 90 degrees
    plt.xticks(rotation=90, ha="right")

    # Setting the size of the graph for when it will be saved to a file
    figure = plt.gcf()
    figure.set_size_inches(24, 8.5)

    # Saving the figure
    plt.savefig(
        f"graphs/research/group/histogram_{column}_{date}.pdf",
        dpi=300,
        format="pdf",
        # bbox_extra_artists=(lgd,),
        bbox_inches="tight",
    )

    plt.show()


# +======================================================================================+
# |  Creates a histogram using binned data as x values and their frequencies as y values |
# |   *This is different from piechart as it would make sense to have 0 counts for bins* |
# +======================================================================================+
def secGetGroupHistogram(input, column):
    df = pd.read_csv(f"csv/{input}.csv")
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
        "500 TB <",
    ]

    df[f"{column}"] = df[f"{column}"].div(terabyte)

    fig, ax = plt.subplots()
    ax.set(
        title=f"{input} {column} Storage in Terabytes",
    )
    ax.hist(df, [0, 1, 50, 100, 200, 300, 400, 500, 600])
    plt.show()
