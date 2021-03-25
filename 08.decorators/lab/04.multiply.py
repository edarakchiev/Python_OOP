import functools


def multiply(times):
    def decorator(func):
        functools.wraps(func)

        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res * times

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))
