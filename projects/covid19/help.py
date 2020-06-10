# Print help from the help.txt file
def print_help():
    hfile = open("help.txt")
    content = hfile.read()
    hfile.close()
    print(content)

##########################
# Test program starts here
##########################

if __name__ == "__main__":
    # execute only if run as a script
    print("Testing...")
    
    if False:
        print_help()