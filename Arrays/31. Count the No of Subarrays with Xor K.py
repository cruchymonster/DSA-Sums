def brute(a, b):
    n = len(a)
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            xorr = 0
            for k in range(i, j+1):
                xorr = xorr ^ a[k]
            if xorr == b:
                cnt += 1
    return cnt

def better(a, b):
    n = len(a)
    cnt = 0
    for i in range(n):
        xorr = 0
        for j in range(i, n):
            xorr = xorr ^ a[j]
            if xorr == b:
                cnt += 1
    return cnt

def optimal(a,b):
    n = len(a)
    xr = 0
    mpp = dict(int)
    mpp[xr] = 1
    cnt = 0
    for i in range(n):
        xr = xr^a[i]
        x = xr^b
        cnt += mpp[x]
        mpp[xr] = 1
    return cnt


a = [4, 2, 2, 6, 4]
k = 6
ans = brute(a,k)
print(ans)
ans1 = better(a,k)
print(ans1)
ans2 = optimal(a,k)
print(ans2)
