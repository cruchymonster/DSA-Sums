def brute(arr, k):
    n = len(arr)
    length = 0
    for i in range(n):
        for j in range(i,n):
            s = 0
            for K in range(i,j+1):
                s += arr[K]
            if s == k:
                length = max(length, j-i+1)
    return length

def brute2(arr, k):
    n = len(arr)
    length = 0
    for i in range(n):
        s = 0
        for j in range(i,n):
            s += arr[j]
            if s == k:
                length = max(length, j-i+1)
    return length

def optimal(arr, k ):
    n = len(arr)
    left, right = 0,0
    summ = arr[0]
    maxlen = 0
    while right <= n:
        while left <= right and summ > k:
            summ -= arr[left]
            left += 1
        if summ == k:
            maxlen = max(maxlen, right - left + 1)
        right += 1
        if right < n:
            summ += arr[right]
    return maxlen


a = [2, 3, 5, 1, 9]
key = 5
ans = brute(a, key)
print(ans)
ans1 = brute2(a, key)
print(ans1)
ans2 = optimal(a, key)
print(ans2)
