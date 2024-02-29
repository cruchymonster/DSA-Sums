import math

def brute(n):
    ans = 0
    for i in range(1, n+1):
        val = i * i
        if val <= n:
            ans = i
        else:
            break
    return ans

def optimal(n):
    ans = int(math.sqrt(n))
    return ans

n = 24
ans = brute(n)
