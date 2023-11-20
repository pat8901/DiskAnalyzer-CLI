import sys
import readline
import src.tools
import src.writer
import src.bar
import src.histogram
import src.command_line
import click

all_colors = (
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "bright_black",
    "bright_red",
    "bright_green",
    "bright_yellow",
    "bright_blue",
    "bright_magenta",
    "bright_cyan",
    "bright_white",
)


@click.group()
def main():
    """Program to generate graphs of disk storage usage"""
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

    for color in all_colors:
        click.echo(click.style(f"I am colored {color}", fg=color))
    for color in all_colors:
        click.echo(click.style(f"I am colored {color} and bold", fg=color, bold=True))
    for color in all_colors:
        click.echo(click.style(f"I am reverse colored {color}", fg=color, reverse=True))

    click.echo(click.style("I am blinking", blink=True))
    click.echo(click.style("I am underlined", underline=True))

    src.writer.generateReports(
        "documents/reports/Storage_Rep_2023-08-10.pdf", "2023-08-10"
    )
    src.bar.getUserBarCharts("research", "2023-08-10")


@main.command()
def test():
    print("hello")


@main.command()
def test2():
    print("world!")


if __name__ == "__main__":
    main()
