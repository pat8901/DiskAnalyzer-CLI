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
# |             This function may be helpful in adding labels to graphs                  |
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
