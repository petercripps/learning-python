# Reads arguments passed into a Python script and put in a dict
import sys
debug = True
 
def read_args(args):
    argdict = {"country": "", "province": "", "date": "", "year": 0}
    
    # If no arguments return empty dict
    if len(args) == 1:
        print("No arguments provided, try using '-h'")
        return{}
    
    # If first argument is -h print help and return empty dict
    if args[1] == '-h':
        print_help()
        return{}
    
    # Read arguments
    try:
        i = 1
        while i < len(args):    
            if args[i] == '-c':
                argdict["country"] = args[i + 1]
                i += 1
            elif args[i] == '-p':
                argdict["province"] = args[i + 1]
                i += 1   
            elif args[i] == '-d':
                argdict["date"] = args[i + 1]
                i += 1
            elif args[i] == '-y':
                argdict["year"] = int(args[i + 1])
                i += 1
            else:
                print("Unknown argument", args[i])
            i += 1    
    except IndexError:
        print("Invalid or missing argument")
    return argdict

def print_help():
    print("Usage: arguments.py -c <country> -p <province> -d <date> -y <year>")

#####################
# Program starts here
#####################

if debug:
    # Print info on arguments
    print ('Total number of arguments:', format(len(sys.argv)))
    print ('Argument type:', type(sys.argv))
    print('Arguments:', sys.argv)

dict = read_args(sys.argv)
if debug:
    print(dict)