# Collect random phrases and print out once finished.
store = []

def concat(inp):
    store.append(inp.capitalize())

def printphrases():
    for index in store:
        print(index)

inp = ''
while inp != '\end':
    inp = input("Say something: ")
    if inp != '\end':
        concat(inp)

printphrases()