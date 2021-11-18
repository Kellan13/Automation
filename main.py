from helper_code import shared_functions
from compress import compress
from project import project
from uncompress import uncompress
# from upload import upload
import sys


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        args = sys.argv[2:]  # Trim the name of the function (main.py) as well as the automation command
        if command == 'compress':
            shared_functions.check_error(compress.main(args))
        elif command == 'project':
            shared_functions.check_error(project.main(args))
        elif command == 'uncompress':
            shared_functions.check_error(uncompress.main(args))


if __name__ == '__main__':
    main()
