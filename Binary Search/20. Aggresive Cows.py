def canWePlace(stalls, dist, cows):
    n = len(stalls)
    cntCows = 1
    last = stalls[0]
    for i in range(1, n):
        if stalls[i] - last >= dist:
            cntCows += 1
            last = stalls[i]
        if cntCows >= cows:
            return True
    return False

def brute(stalls, k):
    n = len(stalls)
    stalls.sort()
    limit = stalls[n - 1] - stalls[0]
    for i in range(1, limit + 1):
        if not canWePlace(stalls, i, k):
            return i - 1
    return limit

def optimal(stalls, k):
    n = len(stalls)
    stalls.sort()
    low = 1
    high = stalls[n - 1] - stalls[0]
    while low <= high:
        mid = (low + high) // 2
        if canWePlace(stalls, mid, k):
            low = mid + 1
        else:
            high = mid - 1
    return high

stalls = [0, 3, 4, 7, 10, 9]
k = 4
ans = brute(stalls, k)
