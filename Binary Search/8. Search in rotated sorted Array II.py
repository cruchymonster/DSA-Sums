def brute(arr, k):
    for num in arr:
        if num == k:
            return True
    return False

def optimal(arr,k):
    n = len(arr)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return True
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue
        if arr[low] <= arr[mid]:
            if arr[low] <= k <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= k <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return False

arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
k = 3
ans = brute(arr, k)
