def brute(arr, k):
    n = len(arr)
    howMany = [0] * (n - 1)
    for gasStations in range(1, k + 1):
        maxSection = -1
        maxInd = -1
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            seclen = diff / (howMany[i] + 1)
            if seclen > maxSection:
                maxSection = seclen
                maxInd = i
        howMany[maxInd] += 1
    maxAns = -1
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        seclen = diff / (howMany[i] + 1)
        maxAns = max(maxAns, seclen)
    return maxAns

def numof(dist, arr):
    n = len(arr)  # size of the array
    cnt = 0
    for i in range(1, n):
        noinbtw = ((arr[i] - arr[i - 1]) / dist)
        if (arr[i] - arr[i - 1]) == (dist * noinbtw):
            noinbtw -= 1
        cnt += noinbtw
    return cnt


def optimal(arr, k):
    n = len(arr)
    low = 0
    high = 0
    for i in range(n - 1):
        high = max(high, arr[i + 1] - arr[i])
    diff = 1e-6
    while high - low > diff:
        mid = (low + high) / 2.0
        cnt = numof(mid, arr)
        if cnt > k:
            low = mid
        else:
            high = mid
    return high

arr = [1, 2, 3, 4, 5]
k = 4
ans = brute(arr, k)
