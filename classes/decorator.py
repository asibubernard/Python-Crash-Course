# Python program to illustrate functions
# can be treated as objects

def shout(text):
    return text.upper()


print(shout('hello'))

yell = (shout)

print(yell('Hello'))

# Python program to illustrate functions 
# can be passed as arguments to other functions


def whisper(text):
    return text.lower()

def greet(func):
    # store function in a variable
    greeting = func("""I am created by a function passed as an argument.""")
    print(greeting)

greet(shout)
greet(whisper)


# Python program to illustrate functions
# Functions can return another function
def create_adder(x):
    def adder(y):
        return x + y
    return adder


add_15 = create_adder(15)

print(add_15(10))



# Decorator Syntax
@gfg_decorator
def hello_decorator():
    print("Gfg")


def hello_decorator():
    """This is equal to """

    print("Gfg")

hello_decorator = gfg_decorator(hello_decorator)
