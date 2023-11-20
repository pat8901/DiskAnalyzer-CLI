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
# |             Test function for ploting individual graphs, this is not used            |
# |             There may be some items in here that may be of use later                 |
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
    fig, ax = plt.subplots()

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
