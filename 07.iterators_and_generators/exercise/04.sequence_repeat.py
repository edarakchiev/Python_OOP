class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.max_index = len(self.sequence) - 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration
        self.number -= 1
        if self.index > self.max_index:
            self.index = 0
        el = self.sequence[self.index]
        self.index += 1
        return el


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
