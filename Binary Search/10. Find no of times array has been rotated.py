def brute(arr):
    n = len(arr)
    ans = float('inf')
    index = -1
    for i in range(n):
        if arr[i] < ans:
            ans = arr[i]
            index = i
    return index

def optimal(arr):
    low = 0
    high = len(arr) - 1
    ans = float('inf')
    index = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[low] <= arr[high]:
            if arr[low] < ans:
                index = low
                ans = arr[low]
            break
        if arr[low] <= arr[mid]:
            if arr[low] < ans:
                index = low
                ans = arr[low]
            low = mid + 1
        else:
            if arr[mid] < ans:
                index = mid
                ans = arr[mid]
            high = mid - 1
    return index

arr = [4, 5, 6, 7, 0, 1, 2, 3]
ans = brute(arr)
