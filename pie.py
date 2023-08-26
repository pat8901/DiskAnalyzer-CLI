import sys
from pypdf import PdfReader
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tools
import writer


# +======================================================================================+
# |       Takes in a csv file and a single column and creates a pie chart displaying     |
# |                 the counts of binned data within a specified range                   |
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
    df = df.sort_values(
        f"{column}",
        ascending=False,
    )

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
