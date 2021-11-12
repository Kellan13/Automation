"""
Author: Kellan Anderson
Date: 10/11/21

This program is meant to simplify the compression of files using the tar command. This program will
use the os and sys libraries in order to pull arguments from the command line and execute a tar
command to produce a compressed file.

USE: compress <name> <target> [type]
        name    - The name you want the compressed file to be, not including the file extension**
        target  - The file or directory that you want to compress**
        type    - How you want the file to be compressed. If this argument is left empty the
                  compressed file will default to the .tar.tbz extension. Otherwise the compressed
                  file will have the extension of whatever is passed as this argument
**Required argument

Any errors will be defaulted into the Automation/compress/error.txt
"""


import subprocess


def get_program_option(file_type):
    # Gets the command line argument passed to the program and returns the tar option associated with that extension

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


def main(args):
    # Name of the command
    command = 'tar'

    # Default option
    default = '.tar.tbz '

    # Check to see if the proper amount of arguments have been passed
    if len(args) >= 2:
        name = args[0]
        target = args[1]

        # If there is no specified file extension, compress the target as the default
        if len(args) == 2:
            command += ' -cjvf ' + name + default + target
        else:
            # Check to see if the leading '.' has been passed in the file extension. If not, add it to the beginning
            if '.' in args[2]:
                extension = args[2]
            else:
                extension = '.' + args[2]

            # Get the proper program option
            program_option = get_program_option(args[2])
            if extension[0] != '.':
                extension = '.' + extension

            # Create the command
            command += ' ' + program_option + ' ' + name + extension + ' ' + target

        # Run the command the command and capture the output
        results = subprocess.run(command, capture_output=True, text=True, shell=True)

        # Pass stderr to check_error() and return any errors
        return results

    else:
        # If there are not enough arguments passed, print the correct use
        print('Correct use: compress <name> <target> [type]')


# Used for testing
if __name__ == '__main__':
    # main()
    pass
