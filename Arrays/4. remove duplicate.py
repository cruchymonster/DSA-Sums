def remove(arr, n):
    i = 0
    for j in range(n):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i += 1
    return i


nums = [23, 25, 34, 54, 54, 76, 89]
n = len(nums)
nu = remove(nums, n)
print(nu)
