import sys

def brute(arr):
    n = len(arr)
    mini = sys.maxsize
    for i in range(n):
        mini = min(mini, arr[i])
    return mini

def optimal(arr):
    low = 0
    high = len(arr) - 1
    ans = sys.maxsize
    while low <= high:
        mid = (low + high) // 2
        if arr[low] <= arr[mid]:
            ans = min(ans, arr[low])
            low = mid + 1
        else:
            ans = min(ans, arr[mid])
            high = mid - 1
    return ans

arr = [4, 5, 6, 7, 0, 1, 2, 3]
ans = brute(arr)
