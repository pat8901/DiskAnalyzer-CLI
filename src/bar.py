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
import matplotlib.style as mplstyle
import numpy as np
from . import tools
import os
import click


# TODO if total is zero cancel legend and plot generation. It throws errors if you do.
def getUserBarCharts(group, date):
    """Bar chart function that creates batches of user charts"""
    pd.options.mode.chained_assignment = None  # default='warn'

    year = date[0:4]
    month = tools.getMonth(date)
    save_date = date.replace("-", "")
    if group == "research":
        header = "Full Name"
    elif group == "departments":
        header = "Department"
    else:
        header = "College Name"

    df = pd.read_csv(
        f"./documents/csv/{year}/{month}/{group}_{date}.csv",
        dtype={
            "AFS Groups": float,
            "Users AFS": float,
            "Users Panas.": float,
            "Tot.Used Space": float,
        },
    )
    # Getting the amount of rows in dataframe
    row_count = len(df.index)

    # Check to see if these directories exist. If not, create them
    year_save_path = f"./images/batches/{year}"
    year_is_exist = os.path.exists(year_save_path)
    if not year_is_exist:
        os.makedirs(year_save_path)
    month_save_path = f"./images/batches/{year}/{month}"
    month_is_exist = os.path.exists(month_save_path)
    if not month_is_exist:
        os.makedirs(month_save_path)
    group_save_path = f"./images/batches/{year}/{month}/{group}"
    group_is_exist = os.path.exists(group_save_path)
    if not group_is_exist:
        os.makedirs(group_save_path)

    with click.progressbar(
        range(row_count), label="Generating graphs for each user..."
    ) as bar:
        # Generating a chart for each user found in "users" array
        for user in bar:
            has_data = True
            if df.iloc[user]["Tot.Used Space"] == 0:
                has_data = False

            divisor = tools.getDivisor(df.iloc[user]["Tot.Used Space"])
            counter = tools.getChartCounter(divisor)

            df["AFS Groups"].iloc[user] = df.iloc[user]["AFS Groups"] / divisor
            df["Users AFS"].iloc[user] = df.iloc[user]["Users AFS"] / divisor
            df["Users Panas."].iloc[user] = df.iloc[user]["Users Panas."] / divisor
            df["Tot.Used Space"].iloc[user] = df.iloc[user]["Tot.Used Space"] / divisor

            # print(f"User Index: {user}")
            # print(f'Name {df.iloc[i]["Full Name"]}')
            # print(f'Amount {df.iloc[i]["Tot.Used Space"]}')
            # print(f"divsior: {divisor}")
            # print(f"counter: {counter}")

            fig, ax = plt.subplots()

            # Create bars for AFS Groups, Users AFS, Panasas if data is not 0
            if df.iloc[user]["AFS Groups"] != 0:
                p1 = ax.bar(
                    df.iloc[user][header],
                    df.iloc[user]["AFS Groups"],
                    width=0.5,
                    color="tab:blue",
                    label="AFS Group",
                )
                ax.bar_label(p1, label_type="center")

            if df.iloc[user]["Users AFS"] != 0:
                p2 = ax.bar(
                    df.iloc[user][header],
                    df.iloc[user]["Users AFS"],
                    width=0.5,
                    color="tab:green",
                    bottom=df.iloc[user]["AFS Groups"],
                    label="AFS User",
                )
                ax.bar_label(p2, label_type="center")

            if df.iloc[user]["Users Panas."] != 0:
                p3 = ax.bar(
                    df.iloc[user][header],
                    df.iloc[user]["Users Panas."],
                    width=0.5,
                    color="orange",
                    bottom=df.iloc[user]["AFS Groups"] + df.iloc[user]["Users AFS"],
                    label="Panasas User",
                )
                ax.bar_label(p3, label_type="center")

            # Setting yaxis label and plot title
            ax.set(
                ylabel=counter,
                title=f"{df.iloc[user][header]}'s Storage Amounts {date}",
            )
            # Setting axis limits
            ax.set_xlim(left=-0.7, right=0.7)
            ylimits = ax.get_ylim()
            ax.set_ylim(bottom=None, top=(ylimits[1] + ylimits[1] * 0.15))
            # Displaying total on top of bar
            total = np.float64(
                np.format_float_positional(df.iloc[user]["Tot.Used Space"], precision=4)
            )
            ax.text(
                0,
                total + (total * 0.07),
                f"Total: {total}",
                ha="center",
                weight="bold",
                color="black",
            )
            if has_data == True:
                legend = ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

                name = df.iloc[user][header]
                save_name = name.replace(" ", "_")
                plt.savefig(
                    f"./images/batches/{year}/{month}/{group}/{save_name}_{save_date}.png",
                    dpi=300,
                    format="png",
                    bbox_extra_artists=(legend,),
                    bbox_inches="tight",
                )
                plt.close(fig)
            else:
                name = df.iloc[user][header]
                save_name = name.replace(" ", "_")
                plt.savefig(
                    f"./images/batches/{year}/{month}/{group}/{save_name}_{save_date}.png",
                    dpi=300,
                    format="png",
                    bbox_inches="tight",
                )
                plt.close(fig)


def dynamic_getUserBarCharts(year, month, date, name, group):
    """Function for when getting a user's storage bar chart dynamically

    *Note* to fix the small bar issue. I could choose to not display if the bar value is below a certain
    threshhold which dynamicall changes based on the divsor unit or maybe the other values of the bars
    """
    # Setting backend to a non-interactive backend. This cuts down on graph generation time
    matplotlib.use("agg")
    # These seem to have no affect. look into more before deleting
    matplotlib.rcParams["path.simplify"] = True
    # These seem to have no affect. look into more before deleting
    matplotlib.rcParams["path.simplify_threshold"] = 1.0
    # These seem to have no affect. look into more before deleting
    mplstyle.use("fast")

    # Finding the specified file and loading into dataframe
    # Setting parent path
    parent_path = os.listdir(f"./documents/csv/{year}/{month}")
    # Sets proper csv header depending on the active group
    if group == "research":
        header = "Full Name"
    elif group == "departments":
        header = "Department"
    else:
        header = "College Name"

    my_files = []
    # Checking each file in parent path if it matches search string
    for file in parent_path:
        if file.startswith(f"{group}_{date}"):
            my_files.append(file)

    df = pd.read_csv(f"./documents/csv/{year}/{month}/{my_files[0]}")
    user_csv_index = df[df[header] == f"{name}"].index[0]
    divisor = tools.getDivisor(df.iloc[user_csv_index]["Tot.Used Space"])
    unit = tools.getChartCounter(divisor)
    save_name = name.replace(" ", "_")
    save_date = date.replace("-", "")

    # Dividing the cells the current selected row by the divisor
    df["AFS Groups"] = df["AFS Groups"].div(divisor)
    df["Users AFS"] = df["Users AFS"].div(divisor)
    df["Users Panas."] = df["Users Panas."].div(divisor)
    df["Tot.Used Space"] = df["Tot.Used Space"].div(divisor)
    csv_totals = np.array(df["Tot.Used Space"])
    total = csv_totals[user_csv_index]

    fig, ax = plt.subplots()

    # Create bars for AFS Groups, Users AFS, Panasas if data is not 0
    if df.iloc[user_csv_index]["AFS Groups"] != 0:
        p1 = ax.bar(
            df.iloc[user_csv_index][header],
            df.iloc[user_csv_index]["AFS Groups"],
            width=0.5,
            color="tab:blue",
            label="AFS Group",
        )
        ax.bar_label(p1, label_type="center")
    if df.iloc[user_csv_index]["Users AFS"] != 0:
        p2 = ax.bar(
            df.iloc[user_csv_index][header],
            df.iloc[user_csv_index]["Users AFS"],
            width=0.5,
            color="tab:green",
            bottom=df.iloc[user_csv_index]["AFS Groups"],
            label="AFS User",
        )
        ax.bar_label(p2, label_type="center")
    if df.iloc[user_csv_index]["Users Panas."] != 0:
        p3 = ax.bar(
            df.iloc[user_csv_index][header],
            df.iloc[user_csv_index]["Users Panas."],
            width=0.5,
            color="tab:orange",
            bottom=df.iloc[user_csv_index]["AFS Groups"]
            + df.iloc[user_csv_index]["Users AFS"],
            label="Panasas User",
        )
        ax.bar_label(p3, label_type="center")

    # Setting axis and title labels
    ax.set(ylabel=unit, title=f"{df.iloc[user_csv_index][header]}'s Storage Amounts")
    # Setting axis limits
    ax.set_xlim(left=-0.7, right=0.7)
    ylimits = ax.get_ylim()
    ax.set_ylim(bottom=None, top=(ylimits[1] + ylimits[1] * 0.15))
    # Displaying total on top of bar
    total = np.float64(
        np.format_float_positional(total, precision=4)
    )  # Do I need this?
    ax.text(
        0,
        total + (total * 0.07),
        f"Total: {total}",
        ha="center",
        weight="bold",
        color="black",
    )
    # lgd = ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    lgd = ax.legend(bbox_to_anchor=(1, 1), prop={"size": 6})

    # Checking to see if year, month, and group directorys exist. If not, create them
    year_save_path = f"./images/userStorageCharts/{year}"
    year_is_exist = os.path.exists(year_save_path)
    if not year_is_exist:
        os.makedirs(year_save_path)
    month_save_path = f"./images/userStorageCharts/{year}/{month}"
    month_is_exist = os.path.exists(month_save_path)
    if not month_is_exist:
        os.makedirs(month_save_path)
    group_save_path = f"./images/userStorageCharts/{year}/{month}/{group}"
    group_is_exist = os.path.exists(group_save_path)
    if not group_is_exist:
        os.makedirs(group_save_path)

    fig.savefig(
        # f"./images/userStorageCharts/{year}/{month}/{group}/{df.iloc[user_csv_index][header]}_user_report.png",
        f"./images/userStorageCharts/{year}/{month}/{group}/{save_name}_{save_date}.png",
        dpi=150,
        format="png",
        bbox_extra_artists=(lgd,),
        # bbox_inches="tight", # not havng this may make saving faster
    )


def test_getUserBarCharts(input):
    """Testing function for when getting a user's bar chart of storages

    Only creates one user at a time. This function is used as a testing ground
    before implementing the function into production
    """
    date = input[9:]  # Parsing the date from input
    i = 0  # Selecting row index in dataframe
    # Read csv file into pandas dataframe
    df = pd.read_csv(f"./documents/csv/2023/2023_07_01/{input}.csv")

    # Getting the divisor to divide row by
    divisor = tools.getDivisor(df.iloc[i]["Tot.Used Space"])
    # Getting the unit the numbers are in
    counter = tools.getChartCounter(divisor)
    # Getting the abbreviated unit
    # unit = plots.tools.getUnit(counter)

    # Dividing the cells the current selected row by the divisor
    df["AFS Groups"] = df["AFS Groups"].div(divisor)
    df["Users AFS"] = df["Users AFS"].div(divisor)
    df["Users Panas."] = df["Users Panas."].div(divisor)
    df["Tot.Used Space"] = df["Tot.Used Space"].div(divisor)

    # Using numpy to create an array to house total values.
    array = np.array(df["Tot.Used Space"])
    total = array[i]

    # print(f"User index: {i}")
    fig, ax = plt.subplots()  # Instantiating the plot interface

    # Create bars for AFS Groups, Users AFS, Panasas if data is not 0
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

    # Setting yaxis label and title
    ax.set(ylabel=counter, title=f"{df.iloc[i]['Full Name']}'s Storage Amounts")
    # Setting axis limits
    ax.set_xlim(left=-0.7, right=0.7)
    ylimits = ax.get_ylim()  # getting the current yaxis limits
    ax.set_ylim(bottom=None, top=(ylimits[1] + ylimits[1] * 0.15))
    # Displaying total on top of bar
    total = np.float64(np.format_float_positional(total, precision=4))
    # print(total)
    ax.text(
        0,
        total + (total * 0.07),
        f"Total: {total}",
        ha="center",
        weight="bold",
        color="black",
    )
    # Generating legend
    lgd = ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    # Saving the figure
    plt.savefig(
        f"../images/userStorageCharts/{df.iloc[i]['Full Name']}_user_report_{date}.png",
        dpi=300,
        format="png",
        bbox_extra_artists=(lgd,),
        bbox_inches="tight",
    )
