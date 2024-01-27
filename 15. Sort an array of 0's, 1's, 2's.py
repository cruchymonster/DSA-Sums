def brute(arr):
    arr.sort()

def better(arr):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    for num in arr:
        if num == 0:
            cnt0 += 1
        if num == 1:
            cnt1 += 1
        if num == 2:
            cnt2 += 1
    for i in range(cnt0):
        arr[i] = 0
    for i in range(cnt0, cnt0+cnt1):
        arr[i] = 1
    for i in range(cnt0+cnt1, len(arr)):
        arr[i] = 2


nums = [1,2,1,0,2,0,1,0,2,0]
brute(nums)
print(nums)
better(nums)
print(nums)
