import math

n = int(input())
if n < 2:
    print("NO")
else:
    is_prime = True
    limit = int(math.isqrt(n))
    
    for i in range(2, limit + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("YES")
    else:
        print("NO")