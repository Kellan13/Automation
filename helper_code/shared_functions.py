from datetime import datetime
import pathlib


def check_error(error):
    # Directs any errors to the designated error file and quits the program
    try:
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
    except TypeError:
        pass
    quit()
