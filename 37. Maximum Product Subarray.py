def brute(a):
    result = float('-inf')
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            prod = 1
            for k in range(i,j+1):
                prod *= a[k]
            result = max(result, prod)
    return result

def better(a):
    result = a[0]
    n = len(a)
    for i in range(n-1):
        p = a[i]
        for j in range(i+1, n):
            result = max(result, p)
            p *= nums[j]
        result = max(result, p)
    return result

def optimal(a):
    n = len(a)
    pre, suff = 1, 1
    ans = float('-inf')
    for i in range(n):
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1
        pre *= a[i]
        suff *= a[n-i-1]
        ans = max(ans, max(pre,suff))
    return ans


nums = [1, 2, -3, 0, -4, -5]
ans = brute(nums)
print(ans)
ans1 = better(nums)
print(ans1)
ans2 = optimal(nums)
print(ans2)
