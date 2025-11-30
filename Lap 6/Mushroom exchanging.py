n, k = map(int, input().split())

total_days = 0
stems = 0
while n > 0:
    total_days += n
    stems += n 
    n = stems // k

    stems = stems % k

print(total_days)