def brute(arr, d):
    n = len(arr)
    d = d % n
    temp = [0] * d
    j = 0
    for i in range(d):
        temp[i] = arr[i]
    for i in range(d,n):
        arr[i-d] = arr[i]
    for i in range(n-d,n):
        arr[i] = temp[j]
        j += 1
    for i in arr:
        print(i)


def optimal(arr, start, end):
    while start <= end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


nums = [12, 43, 54, 23, 76, 64]
nu = 2
brute(nums, nu)
