def possible(arr, day, m, k):
    n = len(arr)
    cnt = 0
    noOfB = 0
    for i in range(n):
        if arr[i] <= day:
            cnt += 1
        else:
            noOfB += cnt // k
            cnt = 0
    noOfB += cnt // k
    return noOfB >= m

def brute(arr, k, m):
    val = m * k
    n = len(arr)
    if val > n:
        return -1
    mini = float('inf')
    maxi = float('-inf')
    for i in range(n):
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])
    for i in range(mini, maxi+1):
        if possible(arr, i, m, k):
            return i
    return -1

def optimal(arr, k, m):
    val = m * k
    n = len(arr)
    if val > n:
        return -1
    mini = float('inf')
    maxi = float('-inf')
    low = mini
    high = maxi
    while low <= high:
        mid = (low + high) // 2
        if possible(arr, mid, m, k):
            high = mid - 1
        else:
            low = mid + 1
    return low


arr = [7, 7, 7, 7, 13, 11, 12, 7]
k = 3
m = 2
ans = brute(arr, k, m)
