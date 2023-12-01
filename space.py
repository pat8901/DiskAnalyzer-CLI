"""
Copyright (c) 2023 Patrick O'Brien-Seitz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

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
@click.option("--about", "-a", is_flag=True, help="Tells you about the program")
@click.option(
    "--file",
    "-f",
    type=click.Path(exists=True),
    help="Input a report file to generate data",
)
def main(file, about):
    print("Hello im in main!")
    if file:
        # TODO: parse report
        src.writer.generateReports(file, file.split("/")[-1][-14:-4])
        click.echo(f"File path: {file}")
        click.echo(f"File: {file.split('/')[-1][-14:-4]}")
        getGroup()
    if about:
        info()
    print("exiting...")


def create():
    click.echo(
        click.style(
            f"I am the create command\n",
            bold=True,
        )
    )


def getGroup():
    # value = click.prompt("Please enter a valid integer", type=int)
    # click.confirm("Do you want to continue?", abort=True)
    click.echo(
        click.style(
            f"""What group would you like to create graphs for? 

Options:
    [0] General Stats
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
            case "0":
                print("You chose general stats")
                src.histogram.getStackedGroupHistogram("Researchers", "")
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
                print("Please enter a number between 0-4")
                break

    print(f"You said {group_input}!")


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
    click.echo(
        """
        Copyright (c) 2023 Patrick O'Brien-Seitz

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is furnished
        to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
        THE SOFTWARE.
        """
    )


if __name__ == "__main__":
    main()
