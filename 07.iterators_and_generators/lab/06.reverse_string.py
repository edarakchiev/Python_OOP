def reverse_text(text):
    for c in range(len(text) - 1, -1, -1):
        yield text[c]

for char in reverse_text("step"):
    print(char, end='')
