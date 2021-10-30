"""
Author: Kellan Anderson
Date: 10/11/21

This program is meant to simplify the compression of files using the tar command. This program will
use the os and sys libraries in order to pull arguments from the cammand line and execute a tar
command to produce a compressed file.

USE: compress <name> <target> [type]
        name    - The name you want the compressed file to be, not including the file extention**
        target  - The file or directory that you want to compress**
        type    - How you want the file to be compressed. If this argument is left empty the
                  compressed file will default to the .tar.tbz extention. Otherwise the compressed
                  file will have the extention of whatever is passed as this argument
**Required argument

Any errors will be defaulted into the Automation/compress/error.txt
"""

import subprocess
import sys
import pathlib
from datetime import datetime


def check_error(error):
    # Directs any errors to the designated error file and quits the program
    if len(error):
        # Timestamp reference
        now = datetime.now()
        timestamp = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Path to the error file
        file_loc = str(pathlib.Path(__file__).parent.resolve()) + '/error.txt'

        # Write to the error file
        with open(file_loc, 'a') as file:
            file.write(timestamp + "\n")
            file.write(error)
            file.write("\n")
        print("Command had an error, please read error file at " + file_loc)
        quit()


def get_program_option(file_type):
    # Gets the command line argument passed to the program and returns the tar option associated with that extention

    # List of extensions
    gz_extensions = ['gz', '.gz', 'tar.gz', '.tar.gz']
    other_extensions = ['.tbz', 'tbz', '.tar.tbz', 'tar.tbz', '.bz2', '.tar.bz2', 'bz2', 'tar.bz2']

    # If the extension is a gzip extension, return -zcvf
    if file_type in gz_extensions:
        return '-zcvf'

    # If the extension is any other supported extension
    elif file_type in other_extensions:
        return '-jcvf'

    # If the passed extension is not supported, print the supported extensions and quit the program
    else:
        print('Extension not recognized, supported extensions are')
        for i in gz_extensions:
            print(i, end=', ')
        string = ''
        for i in other_extensions:
            string += i + ', '
        string = string[:-2]
        print(string)
        quit()


def main():
    # Name of the command
    command = 'tar'

    # Default option
    default = '.tar.tbz '
    if len(sys.argv) >= 3:
        name = sys.argv[1]
        target = sys.argv[2]

        # If there is no specified file extension, compress the target as the default
        if len(sys.argv) < 4:
            command += ' -cjvf ' + name + default + target
        else:
            # Check to see if the leading '.' has been passed in the file extension. If not, add it to the beginning
            if '.' in sys.argv[3]:
                extension = sys.argv[3]
            else:
                extension = '.' + sys.argv[3]

            # Get the proper program option
            program_option = get_program_option(sys.argv[3])
            if extension[0] != '.':
                extension = '.' + extension

            # Create the command
            command += ' ' + program_option + ' ' + name + extension + ' ' + target

        # Run the command the command and capture the output
        results = subprocess.run(command, capture_output=True, text=True, shell=True)

        # Pass stderr to check_error() and print stdout
        check_error(results.stderr)
        print(results.stdout)
    else:
        # If there are not enough arguments passed, print the correct use
        print('Correct use: compress <name> <target> [type]')


if __name__ == '__main__':
    main()
