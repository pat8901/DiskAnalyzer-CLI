import sys
from pypdf import PdfReader
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tools
import writer
import bar
import pie
import misc
import histogram


def main():
    # input = sys.argv[1]
    # print(f'You said "{input}"')

    report_date = tools.getReportDate("Storage_Rep_2023-08-10.pdf")

    writer.createFullOutput("Storage_Rep_2023-08-10.pdf")
    writer.createResearchOutput(report_date)
    writer.createDepartmentOutput(report_date)
    writer.createCollegesOutput(report_date)

    writer.csvWriter("research", "research", report_date)
    writer.csvWriter("departments", "departments", report_date)
    writer.csvWriter("colleges", "colleges", report_date)

    # getGroupPieChart("research", "AFS Groups")
    # getGroupPieChart("colleges", "AFS Groups")

    # getUserBarChart("research")
    # test_getUserBarChart("research")
    # bar.finaltestgetUserBarChart("research")

    histogram.getGroupHistogram("research", "AFS Groups", report_date)
    # secGetGroupHistogram('research','AFS Groups')


if __name__ == "__main__":
    main()
