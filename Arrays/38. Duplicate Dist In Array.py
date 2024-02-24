def dist(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                return j-i-1
    return -1

def optimal(arr):
    n = len(arr)
    a = {}
    for i in range(n):
        if arr[i] not in a.keys():
            a[arr[i]] = i
        else:
            return i - a[arr[i]] - 1


nums = [2, 3, 5, 4, 7, 6, 3]
a = dist(nums)
print(a)
b = optimal(nums)
print(b)
