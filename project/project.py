import subprocess


def main(args):
    command_list = []
    if not len(args):
        print('Correct use: project <new project name>')
    else:
        project = 'mkdir ' + args[0]
        command_list.append(project)
        command_list.append(project + '/code')
        command_list.append(project + '/doc')
        command_list.append(project + '/feedback')
        command_list.append('echo ".gitignore" >> ' + args[0] + '/.gitignore')
        command_list.append('touch ' + args[0] + 'README.md')
        result = subprocess.run('; '.join(command_list), capture_output=True, text=True, shell=True)
        return result


if __name__ == '__main__':
    main(['testing'])
