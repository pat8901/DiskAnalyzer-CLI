import sys
import readline
import src.tools
import src.writer
import src.bar
import src.histogram
import src.command_line


def main():
    # file_input = sys.argv[1]
    # print(f'You said "{file_input}"')
    # report_date = tools.getReportDate(file_input)
    # print(f"date: {report_date}")

    # writer.createFullOutput(file_input, report_date)
    # writer.createResearchOutput(report_date)
    # writer.createDepartmentOutput(report_date)
    # writer.createCollegesOutput(report_date)
    # writer.csvWriter("research", "research", report_date)
    # writer.csvWriter("departments", "departments", report_date)
    # writer.csvWriter("colleges", "colleges", report_date)

    # histogram.getGroupTotals("research", "2023-08-10")
    # histogram.getGroupHistogram("research", "AFS Groups", "2023-08-10")
    # histogram.getGroupHistogram("research", "Users AFS", "2023-08-10")
    # histogram.getGroupHistogram("research", "Users Panas.", "2023-08-10")
    # histogram.getStackedGroupHistogram("research", "2023-08-10")

    # command_line.getCommandLine(report_date)

    src.writer.generateReports(
        "documents/reports/Storage_Rep_2023-08-10.pdf", "2023-08-10"
    )


if __name__ == "__main__":
    main()
