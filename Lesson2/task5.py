start = 32
end = 128
symbolsinline = 10
i = start
while True:
    c = symbolsinline
    while c > 0:
        print(f'{i} - {chr(i)}', end=' ')
        i = i + 1
        c = c - 1
        if i > end:
            exit(0)
    print()
