def read_file(myfile):
    file = open(myfile)
    content = file.read()
    file.close()
    print(content)

def char_count(ch, myfile):
    file = open(myfile)
    content = file.read()
    file.close()
    return(content.count(ch))

read_file("file.txt")
print(char_count('a',"file.txt"))

# Opening a file using with statement, read from one file
# and write to another

with open("file.txt", "r") as myfile:
    content = myfile.read()
with open ("first.txt", "w") as myfile:
    myfile.write(content[:90])
