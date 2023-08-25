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

    writer.createFullOutput("Storage_Rep_2023-08-10.pdf")
    writer.createResearchOutput()
    writer.createDepartmentOutput()
    writer.createCollegesOutput()

    writer.csvWriter("research", "research")
    writer.csvWriter("departments", "departments")
    writer.csvWriter("colleges", "colleges")

    # getGroupPieChart("research", "AFS Groups")
    # getGroupPieChart("colleges", "AFS Groups")

    # getUserBarChart("research")
    # test_getUserBarChart("research")
    # bar.finaltestgetUserBarChart("research")
    histogram.getGroupHistogram("research", "AFS Groups")
    # secGetGroupHistogram('research','AFS Groups')


if __name__ == "__main__":
    main()
