"""
Copyright (c) 2024 Patrick O'Brien-Seitz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import sys
from pypdf import PdfReader
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tools
import writer


def getGroupPieChart(input, column):
    """Takes in a csv file and a single column and creates a pie chart displaying the counts of binned data within a specified range"""
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
