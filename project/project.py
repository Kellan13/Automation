import subprocess


def main(args):
    command_list = []

    # If not enough arguments required print the correct use
    if not len(args):
        print('Correct use: project <new project name>')
    else:
        project = 'mkdir ' + args[0]
        command_list.append(project)  # mkdir <project name>
        command_list.append(project + '/code')  # mkdir <project name>/code
        command_list.append(project + '/doc')  # mkdir <project name>/doc
        command_list.append(project + '/feedback')  # mkdir <project name>/feedback
        command_list.append('echo ".gitignore" >> ' + args[0] + '/.gitignore')  # put a .gitignore file into the project
        command_list.append('touch ' + args[0] + 'README.md')  # Create a README file

        # Run the mkdir commands
        result = subprocess.run('; '.join(command_list), capture_output=True, text=True, shell=True)

        # Return any errors
        return result


# Used for testing
if __name__ == '__main__':
    main(['testing'])
