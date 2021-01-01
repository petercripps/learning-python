# See: https://www.datacamp.com/community/tutorials/decorators-python 
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    return 'hello there'

@uppercase_decorator
def say_hi_again():
    return 'hello there, again'

##########################
# Test program starts here
##########################
if __name__ == "__main__":
    decorate = uppercase_decorator(say_hi)
    print(decorate())

    print(say_hi_again())
