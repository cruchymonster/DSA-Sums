import math
def findMax(v):
    maxi = float('-inf')
    n = len(v)
    for i in range(n):
        maxi = max(maxi, v[i])
    return maxi

def cal(v, hourly):
    totalH = 0
    n = len(v)
    for i in range(n):
        totalH += math.ceil(v[i] / hourly)
    return totalH

def brute(v, h):
    maxi = findMax(v)
    for i in range(1, maxi+1):
        reqTime = cal(v, i)
        if reqTime <= h:
            return i
    return maxi

def optimal(v, h):
    low = 1
    high = findMax(v)
    while low <= high:
        mid = (low + high) // 2
        totalH = cal(v, mid)
        if totalH <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low

v = [7, 15, 6, 3]
h = 8
ans = optimal(v, h)
