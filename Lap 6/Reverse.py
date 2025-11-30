a, b = map(int, input().split())

total = a + b

reversed_str = str(total)[::-1]

print(int(reversed_str))