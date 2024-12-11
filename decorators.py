
#the decorators are used to modify the behaviour of function or class. In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.


def announce(f):
    def wrapper():
        print('About to run the function...')
        f()
        print('Done with the function.')
    return wrapper

@announce
def hello():
    print('Hello, world!')

hello()