# Adding tuples with a loop
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1, 4, 5, 6))


def calculate(n, **kwargs): #kwargs = keyword argument
    print(kwargs)
    #for key, value in kwargs.items():
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
        

calculate(2, add=3, multiply=5)

