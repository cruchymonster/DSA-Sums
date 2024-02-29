def brute(arr, n, k):
    first = -1
    last = -1
    for i in range(n):
        if arr[i] == k:
            if first == -1:
                first = i
            last = i
    return (first, last)

arr = [2, 4, 6, 8, 8, 8, 11, 13]
n = 8
k = 8
ans = brute(arr, n, k)
