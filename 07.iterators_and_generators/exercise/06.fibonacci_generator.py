def fibonacci():
    previous_n = 0
    current_num = 1
    while True:
        yield previous_n
        previous_n, current_num = current_num, previous_n + current_num


generator = fibonacci()
for i in range(5):
    print(next(generator))
