# Read command line arguments.
import sys
import yaml
from help import print_help

valid_ops = ["info", "rate"]
valid_rates = ["absolute", "hundred", "million", "change"]
valid_measures = ["Deaths", "Confirmed", "Recovered"]

# Reads a list of arguments or, if none, a file in yaml format and returns
# parameters in a dictionary.
# Parameters:
# args : list
#   The command line arguments
# Returns:
# argdict : dict
#   A dictionary of values read from the command line

def read_args(args):    
    argdict = init_argdict()

    # If no arguments see if there is a YAML file
    if len(args) == 1:
        argdict = read_yaml_file("covid19.yaml")
        print("No arguments provided so using YAML")
    
    # If first argument is -h print help and return empty dict.
    elif args[1] == '-h':
        print_help()
        return {}
    
    # Check if first argument is a valid operation and carry on otherwise
    # first argument is invalid so return an empty dict.
    elif args[1] in valid_ops:
        argdict["operation"] = args[1]
    else:
        print(f"Invalid argument: {args[1]}")
        return {}
    
    # Read remaining arguments starting at second argument
    try:
        i = 2
        while i < len(args):    
            if args[i] == '-c':
                argdict["countries"].append(args[i + 1])
                i += 1
            elif args[i] == '-p':
                argdict["province"] = args[i + 1]
                i += 1  
            elif args[i] == '-d':
                argdict["fdate"] = args[i + 1]
                i += 1
            elif args[i] == '-f':
                argdict["fdate"] = args[i + 1]
                i += 1    
            elif args[i] == '-t':
                argdict["tdate"] = args[i + 1]
                i += 1
            elif args[i] == '-g':
                argdict["graph"] = True
            elif args[i] == '-r':
                if args[i + 1] in valid_rates:
                    argdict["rate"] = args[i + 1]
                else:    
                    print("Invalid rate: ", args[i + 1])
                i += 1  
            elif args[i] == '-m':
                if args[i + 1] in valid_measures:
                    argdict["measure"] = args[i + 1]
                else:    
                    print("Invalid measure: ", args[i + 1])
                i += 1      
            else:
                print("Unknown argument", args[i])
            i += 1    
    except IndexError:
        print("Invalid or missing argument")
    return argdict

# Initialise the arguments dictionsary
# Parameters:
# None
# Returns:
# None

def init_argdict():
    return {"operation": "info", # One of: '' | info | rate
        "countries": [], 
        "province": "", 
        "fdate": "",
        "tdate": "",
        "graph": False,
        "measure": "Deaths", # One of: Deaths | Confirmed | Recovered
        "rate": "absolute"} # One of: absolute | hundred | million | change

# Reads a file in yaml format
# Parameters:
# yfile : str
#   The file location of the yaml file
# Returns:
# data : dict
#   A dictionary of values read from the yaml file

def read_yaml_file(yfile):
    try:
        with open(yfile) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data
    except:
        print("YAML file error: ", yfile)
        return {}

##########################
# Test program starts here
##########################
if __name__ == "__main__":
    # execute only if run as a script
    print("Testing...")
    if False:
        args = read_args(sys.argv)
        print(args)