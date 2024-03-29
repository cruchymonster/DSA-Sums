def brute(arr1, arr2, n, m):
    arr3 = [0] * (m+n)
    left = 0
    right = 0
    index = 0
    while left < n and right < m:
        if arr1[left] <= arr2[right]:
            arr3[index] = arr1[left]
            left += 1
            index += 1
        else:
            arr3[index] = arr2[right]
            right += 1
            index += 1
    while left < n:
        arr3[index] = arr1[left]
        left += 1
        index += 1
    while right < m:
        arr3[index] = arr2[right]
        right += 1
        index += 1
    for i in range(n + m):
        if i < n:
            arr1[i] = arr3[i]
        else:
            arr2[i - n] = arr3[i]

def optimal(arr1, arr2, n, m):
    left = n - 1
    right = 0
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break
    arr1.sort()
    arr2.sort()


arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]
n = 4
m = 3
brute(arr1, arr2, n, m)
print(arr1, arr2)
