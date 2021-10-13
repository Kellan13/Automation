import subprocess
import sys
from datetime import datetime

##
# Type = type of file extention
# passed as .gz, .tar.gz,
##


def check_error(error):
    if len(error):
        now = datetime.now()
        timestamp = now.strftime("%m/%d/%Y, %H:%M:%S")
        with open('error.txt', 'a') as file:
            file.write(timestamp + "\n")
            file.write(error)
            file.write("\n")
        print("Command had an error, please read error file")


def get_file_type(file_type):
    gz_extentions = ['.gz', 'gz', 'tar.gz', '.tar.gz']
    other_extentions = ['.tbz', 'tbz', '.tar.tbz', 'tar.tbz', '.bz2', '.tar.bz2', 'bz2', 'tar.bz2']
    if file_type in gz_extentions:
        return ' -zcvf '
    elif file_type in other_extentions:
        return ' -jcvf '
    else:
        print('Extention not reconized, supported extentions are')
        for i in gz_extentions:
            print(i, end=', ')
        string = ''
        for i in other_extentions:
            string += i + ', '
        string = string[:-2]
        print(string)
        quit()


def main():
    command = 'tar'
    default = '.tar.tbz '
    name = sys.argv[1]
    target = sys.argv[2]
    if len(sys.argv) < 4:
        command += ' -cjvf ' + name + default + target
    else:
        if '.' in sys.argv[3]:
            extension = sys.argv[3]
        else:
            extension = '.' + sys.argv[3]
        type = get_file_type(sys.argv[3])
        command = [command, type, name + extension, target]
    results = subprocess.run(command, capture_output=True, text=True)
    check_error(results.stderr)
    print(command)
    quit()


if __name__ == '__main__':
    main()