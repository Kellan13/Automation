import subprocess


def main(args):
    command = 'tar '
    option = ''

    # Strip the filename from the array
    file = args[0]

    # Check to see if there are valid arguments
    if len(args):

        # Find the file type and set the right uncompress option
        if file[-4:] == '.tbz' or file[-4:] == '.bz2':
            option = '-xjvf '
        elif file[-3:] == '.gz':
            option = '-xzvf '
        else:
            print('Supported extensions are .tbz, .bz2, and .gz')
            quit()

        # Create the command and run it, returning any output
        command += option + args[0]
        return subprocess.run(command, shell=True, text=True)

    else:
        print('Supported extensions are .tbz, .bz2, and .gz')
        quit()
