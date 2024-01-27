def brute(arr, n):
    temp = []
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])
    a = len(temp)
    for i in range(a):
        arr[i] = temp[i]
    for i in range(a,n):
        arr[i] = 0


def optimal(arr, n):
    j = -1
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    for i in range(j+1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1


nums = [2, 0, 5, 3, 0, 6, 0]
brute(nums, len(nums))
for i in nums:
    print(i)

optimal(nums, len(nums))
for i in nums:
    print(i)
