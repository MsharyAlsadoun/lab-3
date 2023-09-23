def repeatHello(func):
    def wrapper():
        x = int(input("Enter a number of repetitions: "))
        for x in range(x):
            func()
    return wrapper

@repeatHello
def hello():
    print('Hello')

hello()