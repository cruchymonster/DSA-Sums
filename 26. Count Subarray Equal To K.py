def brute(arr, k):
    n = len(arr)
    cnt = 0
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j):
                sum = sum + arr[k]
            if sum == k:
                cnt += 1
    return cnt

def better(arr, k):
    n = len(arr)
    cnt = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            if sum == k:
                cnt += 1
    return cnt


arr = [3, 1, 2, 4]
k = 6
ans = brute(arr,k)
print(ans)
ans1 = better(arr,k)
print(ans1)
