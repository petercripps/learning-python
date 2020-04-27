def greet(name):
    if name != "":
        name2 = name.title()
        print("Hi %s " % name2)
    else:
        print("Who are you?")

greet(input("Enter name: "))    