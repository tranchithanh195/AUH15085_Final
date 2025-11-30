n = int(input())

count = 0

for x1 in range(1, n):
    for x2 in range(x1 + 1, n):
        for x3 in range(x2 + 1, n):
            x4 = n - (x1 + x2 + x3)
            if x4 > x3:
                count += 1
            else:
                break

print(count)