def brute(vec, n, k):
    for i in range(n):
        if vec[i] <= k:
            k += 1
        else:
            break
    return k

def optimal(vec, n, k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        missing = vec[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return k + high + 1

vec = [4, 7, 9, 10]
n = 4
k = 4
ans = brute(vec, n, k)
