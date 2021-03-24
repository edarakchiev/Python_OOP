class dictionary_iter:
    def __init__(self, dict_obj):
        self.dict_obj = dict_obj
        self.tuple_obj = [el for el in self.dict_obj.items()]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.tuple_obj):
            raise StopIteration
        tup = self.tuple_obj[self.index]
        self.index += 1
        return tup


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
