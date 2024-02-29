def findDays(weights, cap):
    days = 1
    load = 0
    n = len(weights)
    for i in range(n):
        if load + weights[i] > cap:
            days += 1
            load = weights[i]
        else:
            load += weights[i]
    return days

def brute(weights, d):
    maxi = max(weights)
    summation = sum(weights)
    for i in range(maxi, summation + 1):
        if findDays(weights, i) <= d:
            return i
    return -1

def optimal(weights, d):
    low = max(weights)
    high = sum(weights)
    while low <= high:
        mid = (low + high) // 2
        numberOfDays = findDays(weights, mid)
        if numberOfDays <= d:
            high = mid - 1
        else:
            low = mid + 1
    return low

weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5
ans = brute(weights, d)
