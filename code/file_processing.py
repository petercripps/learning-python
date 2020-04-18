# This module contains examples of reading, writing and 
# appending files in Python.

# Read an existing file
def read_file():
    with open("file.txt") as file:
        content = file.read()
        print(content)

# Create a new file and write some text in it
def write_new_file(txt):
    with open("file.txt", "w") as file:
        content = file.write(txt)

# Append text to an existing file without overwriting it
def append_file(txt):
    with open("file.txt", "a") as file:
        content = file.write(txt)

# Both append and read a file with:
def append_and_read_file(txt):
    with open("file.txt", "a+") as file:
        content = file.write(txt)
        file.seek(0)
        content = file.read()
        print(content)

# Test the functions in this module
write_new_file("Hello, my name is Ethel")
read_file()
append_file("\nNice to meet you Ethel")
append_and_read_file("\nHow are we all?")