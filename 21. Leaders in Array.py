def brute(arr):
    n = len(arr)
    ans = []
    for i in range(n):
        leader = True
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                leader = False
                break
        if leader:
            ans.append(arr[i])
    return ans

def optimal(arr):
    n = len(arr)
    ans = []
    max_elem = arr[n-1]
    ans.append(arr[n-1])
    for i in range(n-2,-1,-1):
        if arr[i] > max_elem:
            ans.append(arr[i])
            max_elem = arr[i]
    return ans


nums = [10, 22, 12, 3, 0, 6]
h = brute(nums)
print(h)
k = optimal(nums)
print(k)
