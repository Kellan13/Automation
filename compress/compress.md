Author: Kellan Anderson
Date: 10/11/21

This program is meant to simplify the compression of files using the tar command. This program will
use the os and sys libraries in order to pull arguments from the cammand line and execute a tar 
command to produce a compressed file.

Added as an alias command by running:
echo "alias compress='python3 <path to automation directory>/Automation/compress/compress.py'" >> ~/.profile

USE: compress <name> <target> [type]
	name 	- The name you want the compressed file to be, not including the file extention**
	target 	- The file or directory that you want to compress**
	type 	- How you want the file to be compressed. If this argument is left empty the 
		  compressed file will default to the .tar.tbz extention. Otherwise the compressed
		  file will have the extention of whatever is passed as this argument
**Required argument

Any errors will be defaulted into the Automation/compress/error.txt
