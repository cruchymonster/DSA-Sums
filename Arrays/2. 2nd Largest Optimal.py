def sec(arr, n):
    l = arr[0]
    sl = -1
    for i in range(n):
        if arr[i] > l:
            sl = l
            l = arr[i]
        elif arr[i] < l and arr[i] > sl:
            sl = arr[i]
    print(sl)


nums = [51, 23, 64, 21, 87, 35, 72]
n = len(nums)
sec(nums, n)
