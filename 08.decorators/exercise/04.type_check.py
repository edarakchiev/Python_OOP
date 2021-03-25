import functools


def type_check(data):
    def decorator(func):
        functools.wraps(func)

        def wrapper(*args, **kwargs):
            if type(*args, **kwargs) == data:
                return func(*args, **kwargs)
            else:
                return "Bad Type"

        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2

print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
