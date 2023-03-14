# Show use of if elif else

# Respond to name in different ways depending on what it is
def namechecker(name):
    me = "Pete"
    if name == "Gwen":
        print("Hi %s my name is %s" % (name, me))
        return True
    elif name == "Tony":
        print("Hi %s do you remember me, it's %s" % (name, me))
        return True
    elif name == "Lesley":
        pet = "dog"
        print("Hi %s how is your %s?" % (name, pet))
        return True
    elif name == "Dave":
        pet = "rabbit"
        print("Hi %s how is your pet %s?" % (name, pet))
        return True
    else:
        print("Sorry, don't recognise you")
        return False

# Keep calling namechecker until a name is not recognised
carryon = True
while carryon:
    name = input("Who are you?")
    carryon = (namechecker(name))