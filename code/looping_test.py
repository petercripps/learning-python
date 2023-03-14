# Show use of for statement

phone_numbers = {"John Smith": "+37682929928", 
    "Marry Simmons": "+423998200919",
    "Harry Tomlinson": "+4476484567239"}

for entry in phone_numbers.items():
    print(entry[0],": ", entry[1])