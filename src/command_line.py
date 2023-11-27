import src.bar
import src.histogram


def getCommandLine(report_date):
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
            src.bar.getUserBarCharts(group, date)
        case "2":
            print("creating indiviual group histogram")
            src.histogram.getGroupHistogram(group, "AFS Groups", date)

        case "3":
            print("Creating stacked histogram")
            src.histogram.getStackedGroupHistogram(group, date)
        case "4":
            print("you choose to quit")
        case _:
            print("you choose invalid option!")


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

# for color in all_colors:
#     click.echo(click.style(f"I am colored {color}", fg=color))
# for color in all_colors:
#     click.echo(click.style(f"I am colored {color} and bold", fg=color, bold=True))
# for color in all_colors:
#     click.echo(click.style(f"I am reverse colored {color}", fg=color, reverse=True))

# click.echo(click.style("I am blinking", blink=True))
# click.echo(click.style("I am underlined", underline=True))

# src.writer.generateReports(
#     "documents/reports/Storage_Rep_2023-08-10.pdf", "2023-08-10"
# )
# src.bar.getUserBarCharts("research", "2023-08-10")
