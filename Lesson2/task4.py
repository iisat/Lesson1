n = int(input('До какого числа считать простые числа: '))

sieve = [i for i in range(n)]
sieve[1] = 0

for i in range(2, n):
    if sieve[i] != 0:
        j = i + i
        while j < n:
            sieve[j] = 0
            j += i

res = [i for i in sieve if i != 0]

print(sieve)
print(res)
print(len(res))
