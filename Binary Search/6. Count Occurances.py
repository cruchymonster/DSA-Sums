def count(arr, n, x):
    cnt = 0
    for i in range(n):
        if arr[i] == x:
            cnt += 1
    return cnt

arr = [2, 4, 6, 8, 8, 8, 11, 13]
n = 8
x = 8
ans = count(arr, n, x)
