# decorator is a python feature that
#lets you modifya function using @ symbol 
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("after")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")

say_hello()  # Output: Before Hello! after