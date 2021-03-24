class vowels:
    VOWELS = {"a", "e", "i", "u", "y", "o", "A", "E", "I", "U", "Y", "O"}

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        chr = self.text[self.index]
        self.index += 1
        if chr not in vowels.VOWELS:
            return self.__next__()
        return chr


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
