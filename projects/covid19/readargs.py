# Read command line arguments.
import sys
from help import print_help

valid_ops = ["info", "rate", "compare"]
argdict = {"operation": "",
    "country": "", 
    "province": "", 
    "date": "",
    "fdate": "",
    "tdate": "",
    "graph": False}

def read_args(args):
    
    # If no arguments return empty dict
    if len(args) == 1:
        print("No arguments provided, try using '-h'")
        return argdict
    
    # If first argument is -h print help and return empty dict. Otherwise should be
    # the operation so check if a valid operation is provided and carry on otherwise
    # first argument is invalid so return an empty dict.
    if args[1] == '-h':
        print_help()
        return argdict
    elif args[1] in valid_ops:
        argdict["operation"] = args[1]
    else:
        print("Invailid argument")
        return argdict
    
    # Read remaining arguments starting at second argument
    try:
        i = 2
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
            elif args[i] == '-f':
                argdict["fdate"] = args[i + 1]
                i += 1    
            elif args[i] == '-t':
                argdict["tdate"] = args[i + 1]
                i += 1
            elif args[i] == '-g':
                argdict["graph"] = True
            else:
                print("Unknown argument", args[i])
            i += 1    
    except IndexError:
        print("Invalid or missing argument")
    return argdict

if __name__ == "__main__":
    # execute only if run as a script
    args = read_args(sys.argv)
    print(args)