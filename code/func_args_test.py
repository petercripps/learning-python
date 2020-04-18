# Functions with variable numbers of arguments
def avg(*args):
    print(args)
    return sum(args)/len(args)

def to_uppercase(*args):
    print(args)
    uppercase = []
    for item in args:
        uppercase.append(item.upper())
    return sorted(uppercase)

# print(avg(3,8,9,7,1,5,6,7,8))
print(to_uppercase("fred", "gail", "emily"))