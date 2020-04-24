# Read arguments passed into script

import sys

country = "NaN"
region = "Nan"
date = "NaN"

index = 1
numargs = len(sys.argv)
while index < numargs:
    try:
        arg = str(sys.argv[index])
        if arg == '-c':
            country = str(sys.argv[index+1])
        elif arg == '-r':
            region = str(sys.argv[index+1])
        elif arg == '-d':
            date = str(sys.argv[index+1])
    except IndexError:
        print("Invalid number of arguments")
    except:
        print("Input error")
    index = index + 2

print(country)
print(region)
print(date)