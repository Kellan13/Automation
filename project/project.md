Author: Kellan Anderson
Date: 10/30/2021

The purpose of this automation is to initialize a new project directory (an example of this 
directory can be found at Automation/project/example_file_structure), create README.md and 
.gitignore files, and run the git init command.

Added as an alias command by running:
echo 'alias project='python3 <path to automation directory>/Automation/project/project.py'" >> ~/.profile

USE: project <name>
	name - name of the new project

Any errors will be directed into the Automation/project/error.txt
