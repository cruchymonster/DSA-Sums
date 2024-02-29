def count(arr, pages):
    n = len(arr)
    students = 1
    pagesStudent = 0
    for i in range(n):
        if pagesStudent + arr[i] <= pages:
            pagesStudent += arr[i]
        else:
            students += 1
            pagesStudent = arr[i]
    return students

def brute(arr, n, m):
    if m > n:
        return -1
    low = max(arr)
    high = sum(arr)
    for pages in range(low, high + 1):
        if count(arr, pages) == m:
            return pages
    return low

def optimal(arr, n, m):
    if m > n:
        return -1
    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low + high) // 2
        students = count(arr, mid)
        if students > m:
            low = mid + 1
        else:
            high = mid - 1
    return low

arr = [25, 46, 28, 49, 24]
n = 5
m = 4
ans = brute(arr, n, m)
