"""
Copyright (c) 2023 Patrick O'Brien-Seitz

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

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os

# import tools


# +======================================================================================+
# |             Creates a histogram of total storage values for the 3 groups             |
# +======================================================================================+
def getGroupTotals(group, year, month, date):
    # Read csv file into pandas dataframe
    df = pd.read_csv(f"csv/{group}_{date}.csv")
    terabyte = 1000000000  # Terabyte definition

    # Converting from KB to TB for each column of data
    df["AFS Groups"] = df["AFS Groups"].div(terabyte)
    df["Users AFS"] = df["Users AFS"].div(terabyte)
    df["Users Panas."] = df["Users Panas."].div(terabyte)
    df["Tot.Used Space"] = df["Tot.Used Space"].div(terabyte)

    # Summing each column
    afs_group_total = df["AFS Groups"].sum()
    afs_user_total = df["Users AFS"].sum()
    panas_total = df["Users Panas."].sum()
    # total = df["Tot.Used Space"].sum()

    fig, ax = plt.subplots()  # Instantiating the plot interface

    ax.set_ylabel("Terabytes", fontsize=16)  # Setting y label unit
    # Setting the title of the plot
    ax.set_title(f"Group Storage Amount ({date})", fontsize=16)
    matplotlib.pyplot.xticks(fontsize=12)  # Setting xtick marks and setting size
    matplotlib.pyplot.yticks(fontsize=14)  # Setting ytick marks and seting size
    # Setting this to True so one can properly layer different parts of the plot
    ax.set_axisbelow(True)
    # Setting the plot to have gridlines for the y axis
    plt.grid(axis="y", color="0.95", zorder=0)

    # Creating bars for each group
    afs_group_bar = ax.bar(
        "AFS Group", afs_group_total, label="AFS Group", width=1, edgecolor="white"
    )
    ax.bar_label(afs_group_bar, label_type="edge", fontsize=16)
    afs_user_bar = ax.bar(
        "AFS User", afs_user_total, label="AFS Group", width=1, edgecolor="white"
    )
    ax.bar_label(afs_user_bar, label_type="edge", fontsize=16)
    panasas_bar = ax.bar(
        "Panasas", panas_total, label="AFS Group", width=1, edgecolor="white"
    )
    ax.bar_label(panasas_bar, label_type="edge", fontsize=16)

    # Setting the size of the graph for when it will be saved to a file
    figure = plt.gcf()
    figure.set_size_inches(24, 8.5)

    # Checking to see if year directory exist
    year_save_path = f"./images/groupStorageCharts/{year}"
    year_is_exist = os.path.exists(year_save_path)
    if not year_is_exist:
        os.makedirs(year_save_path)
        # print(f"Directory {year_save_path} was created!")

    # Checking to see if month directory exist
    month_save_path = f"./images/groupStorageCharts/{year}/{month}"
    month_is_exist = os.path.exists(month_save_path)
    if not month_is_exist:
        os.makedirs(month_save_path)
        # print(f"Directory {month_save_path} was created!")

    # Saving the figure
    plt.savefig(
        f"./images/groupStorageCharts/{year}/{month}/{group}_totals_{date}.png",
        dpi=300,
        format="png",
        bbox_inches="tight",
    )


# +======================================================================================+
# |             Creates a histogram for a single group and single storage type.          |
# |             Uses binned data as x values and their frequencies as y values           |
# +======================================================================================+
def getGroupHistogram(group, column, date):
    # Reads csv file selected by group and date into a pandas dataframe
    df = pd.read_csv(f"csv/{group}_{date}.csv")
    terabyte = 1000000000  # Terabyte definition
    # Bins that values will be compared against
    bins = [0, 0.001, 0.1, 0.5, 1, 4, 10, 20, 50, 10000000]
    # Labels for the bins
    labels = [
        "0-1 GB",
        "1-100 GB",
        "100-500 GB",
        "500-1 TB",
        "1-4 TB",
        "4-10 TB",
        "10-20 TB",
        "20-50 TB",
        "> 50 TB",
    ]

    # Instantiating the plot interface
    fig, ax = plt.subplots()

    # Covert data in column from kilobytes to terabytes
    df[f"{column}"] = df[f"{column}"].div(terabyte)
    # Creating the bins
    df["bin"] = pd.cut(df[f"{column}"], bins, labels=labels, right=False)
    # Counts the frequency of counts within bin ranges
    data = df["bin"].value_counts(sort=False)
    # print(data)

    # *Debugging* Shows full table data. If you were to just print() it would only summerize
    # with pd.option_context("display.max_rows", None, "display.max_columns", None):
    #     print(df)

    # Setting the graph's x/y labels and title
    ax.set_ylabel("Number of Users", fontsize=16)
    # For the "Tot.Used Space" column convert it to its full name for the title
    if column == "Tot.Used Space":
        ax.set_title(f"Total Used Space ({date})", fontsize=16)
    # For every coulmn that is not "Tot.Used Space" set the title as the original
    else:
        ax.set_title(f"{column} ({date})", fontsize=16)

    # Setting the font sizes for the x and y ticks
    matplotlib.pyplot.xticks(fontsize=12)
    matplotlib.pyplot.yticks(fontsize=14)
    # Displaying footnote text letting the user know there is hidden data in the plot as it is insignificant data
    plt.figtext(
        0.12,
        0.01,
        f"*{data[0]} users between 0GB-1GB not displayed",
        horizontalalignment="left",
        fontsize=12,
    )

    # Looping through each bin reating bar plots and adding them to graph
    for i in range(len(data)):
        # Skipping the first bin as it only contains insignificant data which skews the results for the plot
        if i == 0:
            continue
        # Create and plot a bar containing the frequency data for the bin
        else:
            p = ax.bar(
                labels[i],
                data[i],
                label=labels[i],
                width=1,
                edgecolor="white",
            )
            # Labeling the bar
            ax.bar_label(p, label_type="edge", fontsize=16)

    # Rotating x labels 0 degrees
    plt.xticks(rotation=0, ha="center")

    # Setting the size of the graph for when it will be saved to a file
    figure = plt.gcf()
    figure.set_size_inches(24, 8.5)

    # Saving the figure
    plt.savefig(
        f"graphs/research/group_reports/{group}_{column}_histogram_{date}.png",
        dpi=300,
        format="png",
        bbox_inches="tight",
    )
    # plt.show() # Showing the plot


# +======================================================================================+
# |                Creates a stacked histogram containing all storage types.             |
# |             Uses binned data as x values and their frequencies as y values           |
# |          *This needs to be fixed so it can be dynamic in its error correction*       |
# +======================================================================================+
def getStackedGroupHistogram(group, year, month, date):
    df = pd.read_csv(f"./documents/csv/{year}/{month}/{group}_{date}.csv")
    save_date = date.replace("-", "")
    row_count = len(df.index)
    terabyte = 1000000000
    # Colors for the bars
    colors = [
        "tab:blue",
        "orange",
        "tab:green",
        "tab:purple",
        "tab:pink",
        "tab:cyan",
        "tab:gray",
        "tab:brown",
    ]

    hidden_bins = [0, 0.001]  # Bins to hold insignificant data
    hidden_label = ["0GB-1GB"]  # Label for insignificant data
    bins = [0.001, 0.1, 0.5, 1, 4, 10, 20, 50, 10000000]  # Bins for the good data
    # Labels for good data
    labels = [
        "1-100 GB",
        "100-500 GB",
        "500-1 TB",
        "1-4 TB",
        "4-10 TB",
        "10-20 TB",
        "20-50 TB",
        "> 50 TB",
    ]

    # Instantiating the plot interface
    fig, ax = plt.subplots()

    # Covert data in column from kilobytes to terabytes
    df["AFS Groups"] = df["AFS Groups"].div(terabyte)
    df["Users AFS"] = df["Users AFS"].div(terabyte)
    df["Users Panas."] = df["Users Panas."].div(terabyte)
    df["Tot.Used Space"] = df["Tot.Used Space"].div(terabyte)

    # Bins that contain the data that we are looking for
    df["bin_AFS_Groups"] = pd.cut(df["AFS Groups"], bins, labels=labels, right=False)
    df["bin_Users_AFS"] = pd.cut(df["Users AFS"], bins, labels=labels, right=False)
    df["bin_Users_Panas."] = pd.cut(
        df["Users Panas."], bins, labels=labels, right=False
    )
    df["bin_total"] = pd.cut(df["Tot.Used Space"], bins, labels=labels, right=False)

    # Bins that contain insignificant data that skews the plot. This data will be hidden, but mentioned in a footnote
    df["bin_AFS_Groups_unused"] = pd.cut(
        df["AFS Groups"], hidden_bins, labels=hidden_label, right=False
    )
    df["bin_Users_AFS_unused"] = pd.cut(
        df["Users AFS"], hidden_bins, labels=hidden_label, right=False
    )
    df["bin_Users_Panas._unused"] = pd.cut(
        df["Users Panas."], hidden_bins, labels=hidden_label, right=False
    )
    df["bin_total_unused"] = pd.cut(
        df["Tot.Used Space"], hidden_bins, labels=hidden_label, right=False
    )

    # Counts the frequency of counts within bin ranges
    data_AFS_Groups = df["bin_AFS_Groups"].value_counts(sort=False)
    data_Users_AFS = df["bin_Users_AFS"].value_counts(sort=False)
    data_Users_Panas = df["bin_Users_Panas."].value_counts(sort=False)
    # data_total = df["bin_total"].value_counts(sort=False) # Not used, keep for information sake

    data_AFS_Groups_unused = df["bin_AFS_Groups_unused"].value_counts(sort=False)
    data_Users_AFS_unused = df["bin_Users_AFS_unused"].value_counts(sort=False)
    data_Users_Panas_unused = df["bin_Users_Panas._unused"].value_counts(sort=False)
    # data_total_unused = df["bin_total_unused"].value_counts(sort=False) # Not used, keep for information sake

    # *Debugging* Shows full table data. If you were to just print() it would only summerize
    # with pd.option_context("display.max_rows", None, "display.max_columns", None):
    #     print(df)

    # Setting the graph's x/y labels and title
    ax.set_ylabel("Number of Users", fontsize=16)
    ax.set_title(
        f"Combined Counts From AFS Groups, Users AFS, and Users Panasas ({date})",
        fontsize=16,
    )

    # Creating bar plots and adding them to graph !!!Check to make sure that the if/for statements are indeed reduced!!!
    for i in range(len(data_AFS_Groups)):
        # Run only if not the first column i.e. insignificant data
        if data_AFS_Groups[i] != 0:
            # Creating the bar
            p0 = ax.bar(
                labels[i],
                data_AFS_Groups[i],
                label=labels[i],
                width=1,
                color=colors[0],
                edgecolor="black",
            )
            # If i not in the list then give it a label !!!This is where I needs to fix to make it more dynamic!!!
            if i not in [5, 6, 7]:
                ax.bar_label(p0, label_type="center", fontsize=16)
        # Run only if not the first column i.e. insignificant data
        if data_Users_AFS[i] != 0:
            # Creating the bar
            p1 = ax.bar(
                labels[i],
                data_Users_AFS[i],
                label=labels[i],
                width=1,
                bottom=data_AFS_Groups[i],
                color=colors[1],
                edgecolor="black",
            )
            # If i not in the list then give it a label !!!This is where I needs to fix to make it more dynamic!!!
            if i not in [5, 6, 7]:
                ax.bar_label(p1, label_type="center", fontsize=16)
        # Run only if not the first column i.e. insignificant data
        if data_Users_Panas[i] != 0:
            # Creating the bar
            p2 = ax.bar(
                labels[i],
                data_Users_Panas[i],
                label=labels[i],
                width=1,
                bottom=data_AFS_Groups[i] + data_Users_AFS[i],
                color=colors[2],
                edgecolor="black",
            )
            # If "i" is not in the list then give it a label !!!This is where I needs to fix to make it more dynamic!!!
            if i not in [5, 6, 7]:
                ax.bar_label(p2, label_type="center", fontsize=16)

        # Get the total for each stacked bar
        total = data_AFS_Groups[i] + data_Users_AFS[i] + data_Users_Panas[i]
        # Label the stacked bar with the total
        ax.text(
            i,
            total + 5,
            f"Total: {total}",
            ha="center",
            weight="bold",
            color="black",
        )
    # Setting this to True so one can properly layer different parts of the plot
    ax.set_axisbelow(True)

    # Setting horizontal lines
    plt.grid(axis="y", color="0.95", zorder=0)
    # Setting the x/y ticks and font sizes
    matplotlib.pyplot.xticks(fontsize=12)
    matplotlib.pyplot.yticks(fontsize=14)
    # Displaying footnote text letting the user know there is hidden data in the plot as it is insignificant data
    plt.figtext(
        0.12,
        0.01,
        f"""Note: 
        {row_count} unique users
        {row_count*3} total counts 
        {data_AFS_Groups_unused[0]+data_Users_AFS_unused[0]+data_Users_Panas_unused[0]} counts between 0-1 GB not displayed""",
        horizontalalignment="left",
        fontsize=12,
        color="0.4",
    )
    # Creating a table to house data whose labels where overlapping and could not read. !!!This is an area where it needs to be made dynamic!!!
    plt.table(
        cellText=[
            [data_Users_Panas[5], data_Users_Panas[6], data_Users_Panas[7]],
            [data_Users_AFS[5], data_Users_AFS[6], data_Users_AFS[7]],
            [data_AFS_Groups[5], data_AFS_Groups[6], data_AFS_Groups[7]],
        ],
        colWidths=[0.05] * 3,
        rowLabels=["Users Panasas", "Users AFS", "AFS Groups"],
        rowLoc="left",
        rowColours=["tab:green", "orange", "tab:blue"],
        colLabels=["10-20 TB", "20-50 TB", "> 50 TB"],
        loc="center right",
        zorder=3,
    )

    # Rotating x labels 0 degrees
    plt.xticks(rotation=0, ha="center")

    # Setting the size of the graph for when it will be saved to a file
    figure = plt.gcf()
    figure.set_size_inches(24, 8.5)

    plt.savefig(
        f"images/groupStorageCharts/{group}_{save_date}.png",
        dpi=300,
        format="png",
        bbox_inches="tight",
    )
    plt.close(fig)
