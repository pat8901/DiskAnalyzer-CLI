import sys
import tools
import writer
import bar
import histogram


def main():
    # file_input = sys.argv[1]
    # print(f'You said "{file_input}"')

    # print("Which group would you like to create graphs for?")
    # selection_group = input(
    #     """
    # Choose a number

    # Options:
    # [1] Researchers
    # [2] Departments
    # [3] Colleges
    # """
    # )

    # match selection_group:
    #     case "1":
    #         print("you choose researchers")
    #         getJob()

    #     case "2":
    #         print("you choose departments")
    #         getJob()
    #     case "3":
    #         print("you choose colleges")
    #         getJob()
    #     case _:
    #         print("you choose invalid option!")

    report_date = tools.getReportDate("reports/Storage_Rep_2023-08-10.pdf")
    writer.createFullOutput("reports/Storage_Rep_2023-08-10.pdf")
    writer.createResearchOutput(report_date)
    writer.createDepartmentOutput(report_date)
    writer.createCollegesOutput(report_date)
    writer.csvWriter("research", "research", report_date)
    writer.csvWriter("departments", "departments", report_date)
    writer.csvWriter("colleges", "colleges", report_date)

    # bar.getUserBarCharts("research", report_date)

    histogram.getStackedGroupHistogram("research", report_date)
    histogram.getGroupHistogram("research", "Users AFS", report_date)
    histogram.getGroupHistogram("research", "Users Panas.", report_date)
    histogram.getGroupHistogram("departments", "AFS Groups", report_date)


def getJob():
    print("Which job would you like to preform?")
    selection_job = input(
        """
    Choose a number

    Options:
    [1] Create a batch of graphs for individual users
    [2] Create a histogram on the frequencies of ranges for the whole group of users  
    [3] Do nothing
    """
    )
    match selection_job:
        case "1":
            print("you choose create batch of graphs")

        case "2":
            print("you choose create a histogram")
        case "3":
            print("you choose to do nothing")
        case _:
            print("you choose invalid option!")


if __name__ == "__main__":
    main()
