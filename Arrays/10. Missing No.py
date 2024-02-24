def brute(arr,n):
    for i in range(1, n+1):
        flag = 0
        for j in range(len(arr)):
            if arr[j] == i:
                flag = 1
                break
        if flag == 0:
            return i
    return -1

def better(arr,n):
    hash = [0] *(n+1)
    for i in range(n-1):
        hash[a[i]] += 1
    for i in range(1,n+1):
        if hash[i] == 0:
            return i

def optimal(arr,n):
    summ = (n*(n+1))//2
    s2 = sum(arr)
    miss = summ - s2
    return miss


N = 5
a = [1, 2, 4, 5]
ans = brute(a, N)
print(ans)
