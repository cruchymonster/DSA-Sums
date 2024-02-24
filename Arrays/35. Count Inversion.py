import math


def brute(a):
    n = len(a)
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                cnt += 1
    return cnt


def optimal(arr, low, mid, high):
    n = len(a)
    temp = []
    left = low
    right = mid + 1
    cnt = 0
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid - left + 1)
            right += 1
    while (left <= mid):
        temp.append(arr[left])
        left += 1
    while (right <= high):
        temp.append(arr[right])
        right += 1
    for i in range(low, high + 1):
        arr[i] = temp[i - low]
    return cnt


def mergeSort(arr, low, high):
    cnt = 0
    if low >= high:
        return cnt
    mid = math.floor((low + high) / 2)
    cnt += mergeSort(arr, low, mid)
    cnt += mergeSort(arr, mid + 1, high)
    cnt += optimal(arr, low, mid, high)
    return cnt


a = [5, 4, 3, 2, 1]
n = 5
ans = brute(a)
print(ans)
ans1 = mergeSort(a, 0, n-1)
print(ans1)
