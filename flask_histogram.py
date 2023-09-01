import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import tools
import base64
import io


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

    # Setting the graph's x/y labels and title
    ax.set_ylabel("Number of Users", fontsize=16)
    ax.set_title(
        f"Combined Counts From AFS Groups, Users AFS, and Users Panasas ({date})",
        fontsize=16,
    )

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

    ax.set_axisbelow(True)

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

    plt.xticks(rotation=0, ha="center")

    # Setting the size of the graph for when it will be saved to a file
    figure = plt.gcf()
    figure.set_size_inches(18, 8.5)

    # Saving the figure
    # plt.savefig(
    #     f"graphs/research/group_reports/{group}_combined_histogram_{date}.pdf",
    #     dpi=300,
    #     format="pdf",
    #     bbox_inches="tight",
    # )


def convertToImage():
    report_date = tools.getReportDate("reports/Storage_Rep_2023-08-10.pdf")
    getStackedGroupHistogram("research", report_date)

    # Save plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, dpi=75, format="png", bbox_inches="tight")
    img.seek(0)

    # Convert BytesIO object to base64 string
    img_b64 = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return img_b64
