import functools


def vowel_filter(func):
    vowels = {"a", "e", "i", "u", "y", "o", "A", "E", "I", "U", "Y", "O"}
    functools.wraps(func)

    def wrapper():
        result = func()
        return [c for c in result if c in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
