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
@click.option("--about", is_flag=True, help="Tells you about the program")
@click.option(
    "--file",
    type=click.Path(exists=True),
    help="Input a report file to generate data",
)
def main(file, about):
    # print("Hello im in main!")
    if file:
        src.writer.generateReports(file, file.split("/")[-1][-14:-4])
        try:
            getGroup(file.split("/")[-1][-14:-4])
        except KeyboardInterrupt:
            print("Exiting...")
            exit()
    elif about:
        info()
    else:
        click.echo(click.style("No [OPTION] provided!", fg="red"))
        click.echo(
            "Please run program with the --help flag to see the availible options."
        )
    # print("exiting...")


def getGroup(date):
    while True:
        click.echo(
            click.style(
                f"""
+-----------------------------------------------+
| Select Group For Graph Creation               |
|-----------------------------------------------|           
|   [1] Researchers                             |
|   [2] Departments                             |
|   [3] Colleges                                |
|                                               |
|   [q] Quit                                    |
+-----------------------------------------------+ 
"""
            )
        )
        group_input = input(">> ")
        match group_input:
            case "1":
                getJob("research", date)
            case "2":
                getJob("departments", date)
            case "3":
                getJob("colleges", date)
            case "q":
                click.echo("quitting...")
                exit()
            case _:
                click.echo(click.style("Invalid option!", fg="red"))


def getJob(group, date):
    year = date[0:4]
    month = src.tools.getMonth(date)

    while True:
        click.echo(
            click.style(
                f"""
Group: {group}           
+-----------------------------------------------+
| Select Job                                    |
|-----------------------------------------------|
|   [1] General Stats                           |
|   [2] Single-User Graph Generation            |
|   [3] Muli-User Graph Generation              |
|                                               |
|   [b] Back                                    |
|   [q] Quit                                    |
+-----------------------------------------------+ 
"""
            )
        )
        group_input = input(">> ")

        match group_input:
            case "1":
                src.histogram.getStackedGroupHistogram(group, year, month, date)
                break
            case "2":
                sorted_users = src.tools.sortUsers(group, year, month, date)
                selected_user = src.tools.selectUser(sorted_users)
                if selected_user == False:
                    continue
                src.bar.dynamic_getUserBarCharts(
                    year, month, date, selected_user, group
                )
                break
            case "3":
                response = click.confirm(
                    "Creating graphs for all users. Can be time consuming. Do you want to continue?",
                    abort=False,
                )
                if response == True:
                    src.bar.getUserBarCharts(group, date)
                    break
                else:
                    continue
            case "b":
                break
            case "q":
                print("quitting")
                exit()
            case _:
                click.echo(click.style("Invalid option!", fg="red"))


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
