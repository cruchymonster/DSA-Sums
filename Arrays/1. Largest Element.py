def largest(arr, n):
    largests = arr[0]
    for i in range(n):
        if arr[i] > largests:
            largests = arr[i]
    print(largests)


nums = [4, 2, 5, 3, 7, 9, 1, 32, 16]
n = len(nums)
largest(nums, n)
