def optimal(nums):
    cnt, maxi = 0, 0
    for i in range(len(nums)):
        if nums[i] == 1:
            cnt += 1
        else:
            cnt = 0
        maxi = max(maxi,cnt)
    return maxi

arr = [1, 1, 0, 1, 1, 1]
a = optimal(arr)
print(a)
