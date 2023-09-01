import sys
import tools
import writer
import bar
import histogram
import readline


def main():
    file_input = sys.argv[1]
    print(f'You said "{file_input}"')
    report_date = tools.getReportDate(file_input)
    print(f"date: {report_date}")

    writer.createFullOutput(file_input, report_date)
    writer.createResearchOutput(report_date)
    writer.createDepartmentOutput(report_date)
    writer.createCollegesOutput(report_date)
    writer.csvWriter("research", "research", report_date)
    writer.csvWriter("departments", "departments", report_date)
    writer.csvWriter("colleges", "colleges", report_date)

    print("Which group would you like to create graphs for? *Choose a number*")
    selection_group = input(
        """
    Options:
    [1] Researchers
    [2] Departments
    [3] Colleges
    [4] Quit
    """
    )

    match selection_group:
        case "1":
            print("you choose researchers")
            group = "research"
            getJob(group, report_date)
        case "2":
            print("you choose departments")
            group = "departments"
            getJob(group, report_date)
        case "3":
            print("you choose colleges")
            group = "colleges"
            getJob(group, report_date)
        case "4":
            print("you choose to quit")
        case _:
            print("you choose invalid option!")


def getJob(group, date):
    print("Which job would you like to preform?")
    selection_job = input(
        """
    Options:
    [1] Create graphs for all users individualy
    [2] Create a histogram on individual category 
    [3] Create a stacked histogram on all three categories 
    [4] Quit
    """
    )
    match selection_job:
        case "1":
            print("you choose create user graphs")
            bar.getUserBarCharts(group, date)
        case "2":
            print("creating indiviual group histogram")
            histogram.getGroupHistogram(group, "AFS Groups", date)

        case "3":
            print("Creating stacked histogram")
            histogram.getStackedGroupHistogram(group, date)
        case "4":
            print("you choose to quit")
        case _:
            print("you choose invalid option!")


if __name__ == "__main__":
    main()
