import functools


def tags(symbol):
    def decorator(func):
        functools.wraps(func)

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{symbol}>{result}</{symbol}>"

        return wrapper
    return decorator



@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))



@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
