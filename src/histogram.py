import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import tools


# +======================================================================================+
# |             Creates a histogram of total storage values for the 3 groups             |
# +======================================================================================+
def getGroupTotals(group, date):
    df = pd.read_csv(f"csv/{group}_{date}.csv")
    terabyte = 1000000000

    # Converting from KB to TB
    df["AFS Groups"] = df["AFS Groups"].div(terabyte)
    df["Users AFS"] = df["Users AFS"].div(terabyte)
    df["Users Panas."] = df["Users Panas."].div(terabyte)
    df["Tot.Used Space"] = df["Tot.Used Space"].div(terabyte)

    afs_group_total = df["AFS Groups"].sum()
    afs_user_total = df["Users AFS"].sum()
    panas_total = df["Users Panas."].sum()
    total = df["Tot.Used Space"].sum()

    fig, ax = plt.subplots()
    ax.set_ylabel("Terabytes", fontsize=16)
    ax.set_title(f"Group Storage Amount ({date})", fontsize=16)
    matplotlib.pyplot.xticks(fontsize=12)
    matplotlib.pyplot.yticks(fontsize=14)
    ax.set_axisbelow(True)
    plt.grid(axis="y", color="0.95", zorder=0)

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

    # total_bar = ax.bar("Total", total, label="AFS Group", width=1, edgecolor="white")
    # ax.bar_label(total_bar, label_type="edge", fontsize=16)

    # Setting the size of the graph for when it will be saved to a file
    figure = plt.gcf()
    figure.set_size_inches(24, 8.5)

    # Saving the figure
    plt.savefig(
        f"graphs/research/group_reports/{group}_totals_{date}.png",
        dpi=300,
        format="png",
        # bbox_extra_artists=(lgd,),
        bbox_inches="tight",
    )

    plt.show()

    print(f"AFS Group:  {afs_group_total}")
    print(f"AFS User:   {afs_user_total}")
    print(f"Panasas:    {panas_total}")
    print(f"Total:      {total}")


# +======================================================================================+
# |  Creates a histogram using binned data as x values and their frequencies as y values |
# |             *bins are auto-made using the hist function instead of bar*              |
# +======================================================================================+
def getGroupHistogram(group, column, date):
    df = pd.read_csv(f"csv/{group}_{date}.csv")
    terabyte = 1000000000
    scott_bins = [0, 0.001, 0.1, 0.5, 1, 4, 10, 20, 50, 10000000]
    scott_labels = [
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

    better_bins = tools.binCreator(80, 2, 0)
    better_bins_labels = tools.binLabelCreator(80, 2, 0)
    fig, ax = plt.subplots()

    # Covert data in column from kilobytes to terabytes
    df[f"{column}"] = df[f"{column}"].div(terabyte)

    # Creates a new column in dataframe with each row having their appropriate bin
    # df["bin"] = pd.cut(
    #     df[f"{column}"], better_bins, labels=better_bins_labels, right=False
    # )

    # Creating the bins
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
        f"graphs/research/group_reports/{group}_{column}_histogram_{date}.png",
        dpi=300,
        format="png",
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
    row_count = len(df.index)
    terabyte = 1000000000
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
    better_bins = tools.binCreator(80, 2, 0)
    better_bins_labels = tools.binLabelCreator(80, 2, 0)
    scott_unused_bins = [0, 0.001]
    scott_unused_labels = ["0GB-1GB"]
    scott_bins = [0.001, 0.1, 0.5, 1, 4, 10, 20, 50, 10000000]
    scott_labels = [
        "1-100 GB",
        "100-500 GB",
        "500-1 TB",
        "1-4 TB",
        "4-10 TB",
        "10-20 TB",
        "20-50 TB",
        "> 50 TB",
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
    ax.set_ylabel("Number of Users", fontsize=16)
    ax.set_title(
        f"Combined Counts From AFS Groups, Users AFS, and Users Panasas ({date})",
        fontsize=16,
    )

    # Creating bar plots and adding them to graph
    # for i in range(len(data)):
    #     p = ax.bar(better_bins_labels[i], data[i], label=better_bins_labels[i], width=1)
    #     ax.bar_label(p, label_type="edge")

    # Creating bar plots and adding them to graph
    for i in range(len(data_AFS_Groups)):
        if data_AFS_Groups[i] != 0:
            p0 = ax.bar(
                scott_labels[i],
                data_AFS_Groups[i],
                label=scott_labels[i],
                width=1,
                color=colors[0],
                edgecolor="black",
            )
            if i not in [5, 6, 7]:
                ax.bar_label(p0, label_type="center", fontsize=16)
        if data_Users_AFS[i] != 0:
            p1 = ax.bar(
                scott_labels[i],
                data_Users_AFS[i],
                label=scott_labels[i],
                width=1,
                bottom=data_AFS_Groups[i],
                color=colors[1],
                edgecolor="black",
            )
            if i not in [5, 6, 7]:
                ax.bar_label(p1, label_type="center", fontsize=16)
        if data_Users_Panas[i] != 0:
            p2 = ax.bar(
                scott_labels[i],
                data_Users_Panas[i],
                label=scott_labels[i],
                width=1,
                bottom=data_AFS_Groups[i] + data_Users_AFS[i],
                color=colors[2],
                edgecolor="black",
            )
            if i not in [5, 6, 7]:
                ax.bar_label(p2, label_type="center", fontsize=16)

        total = data_AFS_Groups[i] + data_Users_AFS[i] + data_Users_Panas[i]
        ax.text(
            i,
            total + 5,
            f"Total: {total}",
            ha="center",
            weight="bold",
            color="black",
        )

    # Legend - Not really needed
    # lgd = ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    # lgd = ax.legend(
    #     [p2, p1, p0],
    #     ["Users Panasas", "Users AFS", "AFS Groups"],
    #     bbox_to_anchor=(0.85, 0.85),
    #     loc="upper left",
    #     fontsize=18,
    # )

    ax.set_axisbelow(True)

    # Setting horizontal lines
    plt.grid(axis="y", color="0.95", zorder=0)
    matplotlib.pyplot.xticks(fontsize=12)
    matplotlib.pyplot.yticks(fontsize=14)
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

    # Rotating x labels 90 degrees
    # plt.xticks(rotation=90, ha="right")
    # plt.yticks(np.arange(0, 195, 5))
    plt.xticks(rotation=0, ha="center")

    # Setting the size of the graph for when it will be saved to a file
    figure = plt.gcf()
    figure.set_size_inches(24, 8.5)

    # Saving the figure
    plt.savefig(
        f"graphs/research/test_reports/{group}_combined_histogram_{date}.png",
        dpi=300,
        format="png",
        # bbox_extra_artists=(lgd,),
        bbox_inches="tight",
    )

    plt.show()
