n = int(input())


n = abs(n)

s = str(n)
total_sum = 0

for char in s:
    total_sum += int(char)

print(total_sum)