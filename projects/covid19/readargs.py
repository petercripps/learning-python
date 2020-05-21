# Read command line arguments.
import sys
import yaml
from help import print_help

valid_ops = ["info", "rate"]

def read_args(args):
    argdict =init_argdict()
    
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
            elif args[i] == '-r':
                argdict["rate"] = args[i + 1]
                i += 1
            else:
                print("Unknown argument", args[i])
            i += 1    
    except IndexError:
        print("Invalid or missing argument")
    return argdict

# Initialise the dictionary containing arguments.
def init_argdict():
        return {"operation": "",
            "countries": [], 
            "province": "", 
            "date": "",
            "fdate": "",
            "tdate": "",
            "graph": False,
            "rate": 'absolute'}

def read_yaml_file(yfile):
    try:
        with open(yfile) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data
    except:
        print("YAML file error")
        return {}

if __name__ == "__main__":
    # execute only if run as a script
    args = read_args(sys.argv)
    print(args)