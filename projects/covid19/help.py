# Print help from the help.txt file
def print_help():
    hfile = open("help.txt")
    content = hfile.read()
    hfile.close()
    print(content)