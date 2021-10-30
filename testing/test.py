import pathlib
print('Script being run', end=' ')
print(pathlib.Path(__file__).parent.resolve())

print('Current working directory', end = ' ')
print(pathlib.Path().resolve())
