import subprocess
import sys
import os
import pathlib
from datetime import datetime

##
# Type = type of file extention
# passed as .gz, .tar.gz,
##


def check_error(error):
    if len(error):
        now = datetime.now()
        timestamp = now.strftime("%m/%d/%Y, %H:%M:%S")
        file_loc = str(pathlib.Path(__file__).parent.resolve()) + '/error.txt'
        with open(file_loc, 'a') as file:
            file.write(timestamp + "\n")
            file.write(error)
            file.write("\n")
        print("Command had an error, please read error file at " + file_loc)
        quit()


def get_file_type(file_type):
    gz_extensions = ['gz', '.gz', 'tar.gz', '.tar.gz']
    other_extensions = ['.tbz', 'tbz', '.tar.tbz', 'tar.tbz', '.bz2', '.tar.bz2', 'bz2', 'tar.bz2']
    if file_type in gz_extensions:
        return '-zcvf'
    elif file_type in other_extensions:
        return '-jcvf'
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
    command = 'tar'
    default = '.tar.tbz '
    if len(sys.argv) >= 3:
        name = sys.argv[1]
        target = sys.argv[2]
        if len(sys.argv) < 4:
            command += ' -cjvf ' + name + default + target
        else:
            if '.' in sys.argv[3]:
                extension = sys.argv[3]
            else:
                extension = '.' + sys.argv[3]
            file_type = get_file_type(sys.argv[3])
            if extension[0] != '.':
                extension = '.' + extension
            command += ' ' + file_type + ' ' + name + extension + ' ' + target
        results = subprocess.run(command, capture_output=True, text=True, shell=True)
        check_error(results.stderr)
        print(results.stdout)
    else:
        print('Correct use: compress <name> <target> [type]')
    quit()


if __name__ == '__main__':
    main()
