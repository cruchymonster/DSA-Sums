def rotate(arr, n):
    temp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr

nums = [23, 43, 15, 62]
n = len(nums)
s = rotate(nums, n)
for i in s:
    print(i)
