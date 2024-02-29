import math
def brute(arr, limit):
    n = len(arr)
    maxi = max(arr)
    for d in range(1, maxi+1):
        sum = 0
        for i in range(n):
            sum += math.ceil(arr[i] / d)
        if sum <= limit:
            return d
    return -1

def sumByD(arr, div):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        total_sum += math.ceil(arr[i] / div)
    return total_sum

def optimal(arr, limit):
    n = len(arr)
    if n > limit:
        return -1
    low = 1
    high = max(arr)
    while low <= high:
        mid = (low + high) // 2
        if sumByD(arr, mid) <= limit:
            high = mid - 1
        else:
            low = mid + 1
    return low

arr = [1, 2, 3, 4, 5]
limit = 8
ans = brute(arr, limit)
