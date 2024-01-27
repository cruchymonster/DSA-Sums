def brute(a):
    n = len(a)
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > 2 * a[j]:
                cnt += 1
    return cnt

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def countPairs(arr, low, mid, high):
    right = mid + 1
    cnt = 0
    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        cnt += (right - (mid + 1))
    return cnt

def optimal(arr, low, high):
    cnt = 0
    if low >= high:
        return cnt
    mid = (low + high) // 2
    cnt += optimal(arr, low, mid)
    cnt += optimal(arr, mid + 1, high)
    cnt += countPairs(arr, low, mid, high)
    merge(arr, low, mid, high)
    return cnt

a = [4, 1, 2, 3, 1]
ans = brute(a)
print(ans)
ans1 = optimal(a, 0, 4)
print(ans1)
