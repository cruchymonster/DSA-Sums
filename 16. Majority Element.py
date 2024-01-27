def brute(arr):
    n = len(arr)
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j] == arr[i]:
                cnt += 1
        if cnt > n//2: return arr[i]
    return -1

def optimal(arr):
    n = len(arr)
    cnt = 0
    el = None
    for i in range(n):
        if cnt == 0:
            cnt = 1
            el = arr[i]
        elif el == arr[i]:
            cnt += 1
        else:
            cnt -= 1
    cnt1 = 0
    for i in range(n):
        if arr[i] == el:
            cnt1 += 1
    if cnt1 > n//2: return el
    return -1


arr = [2, 2, 1, 1, 1, 2, 2, 1, 1]
ans = brute(arr)
print(ans)
ans1 = optimal(arr)
print(ans1)
