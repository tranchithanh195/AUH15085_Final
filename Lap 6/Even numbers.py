n = int(input())

if n % 2 != 0:
    n -= 1

for i in range(n, 1, -2):
    print(i, end=" ")