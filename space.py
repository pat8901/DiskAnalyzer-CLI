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


@click.command()
@click.argument("input", type=click.Path(exists=True), nargs=0)
# @click.Argument("input", type=click.Path(exists=True), nargs={0,1}, required=False)
@click.option(
    "--create",
    type=click.Choice(["Researchers", "Colleges", "Departments"], case_sensitive=False),
    help="Create plots for the given report",
)
@click.option(
    "--about",
    "about",
    "-a",
    is_flag=True,
    show_default=True,
    default=False,
    help="Tells you about the program",
)
def main(input, create, about):
    print("Hello im in main!")
    if about:
        info()
    click.echo(f"file name: {input}")
    click.echo(click.format_filename(input))
    print("exiting...")

    # print(f"group: {create}")
    # click.echo(f"about value: {about}")
    # input = getGroup()
    # file_input = sys.argv[1]
    # print(f'You said "{file_input}"')
    # report_date = tools.getReportDate(file_input)
    # print(f"date: {report_date}")


def create():
    click.echo(
        click.style(
            f"I am the create command\n",
            bold=True,
        )
    )


def info():
    click.echo(
        """
  _____    _         _      _____                _                            _____   _        _____ 
 |  __ \  (_)       | |    |  __ \              | |                          / ____| | |      |_   _|
 | |  | |  _   ___  | | __ | |__) |   __ _    __| |   __ _   _ __   ______  | |      | |        | |  
 | |  | | | | / __| | |/ / |  _  /   / _` |  / _` |  / _` | | '__| |______| | |      | |        | |  
 | |__| | | | \__ \ |   <  | | \ \  | (_| | | (_| | | (_| | | |             | |____  | |____   _| |_ 
 |_____/  |_| |___/ |_|\_\ |_|  \_\  \__,_|  \__,_|  \__,_| |_|              \_____| |______| |_____|
                                                                                                     
                                                                                                     
"""
    )
    click.echo(
        click.style(
            f'Welcome! To get started type "-help" command to see what you can do.\n',
            bold=True,
        )
    )


def getGroup():
    value = click.prompt("Please enter a valid integer", type=int)
    click.confirm("Do you want to continue?", abort=True)
    click.echo(
        click.style(
            f"""What group would you like to create graphs for? 

Options:
    [1] Researchers
    [2] Departments
    [3] Colleges
    [4] Quit""",
            bold=True,
        )
    )
    while True:
        group_input = input("> ")

        match group_input:
            case "1":
                print("you choose create user graphs")
            case "2":
                print("creating indiviual group histogram")

            case "3":
                print("Creating stacked histogram")

            case "4":
                print("you choose to quit")
            case _:
                print("Invalid option!")
                print("Please enter a number between 1-3")
                break

    print(f"You said {group_input}!")


if __name__ == "__main__":
    main()
