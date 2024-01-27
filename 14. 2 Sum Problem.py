def brute(arr, k):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == k:
                return [i, j]
    return [-1,-1]

def optimal(arr, k):
    n = len(arr)
    arr.sort()
    left, right = 0, n-1
    while left < right:
        summ = arr[left] + arr[right]
        if summ == k:
            return [left, right]
        elif summ < k:
            left += 1
        else:
            right -= 1
    return [-1, -1]


nums = [2, 6, 5, 8, 11]
key = 14
ans = brute(nums, key)
print(ans)
ans1 = optimal(nums, key)
print(ans1)
