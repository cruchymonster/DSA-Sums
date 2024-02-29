def brute(arr, n, x):
    for i in range(n):
        if arr[i] > x:
            return i
    return n

def optimal(arr,n,x):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


arr = [3, 5, 8, 15, 19]
n = 5
x = 9
ind = brute(arr, n, x)

