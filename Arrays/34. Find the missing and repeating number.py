def brute(a):
    n = len(a)
    repeating, missing = -1, -1
    for i in range(1, n+1):
        cnt = 0
        for j in range(n):
            if a[j] == i:
                cnt += 1
        if cnt == 2:
            repeating = i
        elif cnt == 0:
            missing = i
        if repeating != -1 and missing != -1:
            break
    return [repeating, missing]

def better(a):
    n = len(a)
    hash = [0] * (n + 1)
    for i in range(n):
        hash[a[i]] += 1
    repeating, missing = -1, -1
    for i in range(1, n + 1):
        if hash[i] == 2:
            repeating = i
        elif hash[i] == 0:
            missing = i
        if repeating != -1 and missing != -1:
            break
    return [repeating, missing]

def optimal(a):
    n = len(a)
    SN = (n * (n + 1)) // 2
    S2N = (n * (n + 1) * (2 * n + 1)) // 6
    S, S2 = 0, 0
    for i in range(n):
        S += a[i]
        S2 += a[i] * a[i]
    val1 = S - SN
    val2 = S2 - S2N
    val2 = val2 // val1
    x = (val1 + val2) // 2
    y = x - val1
    return [x, y]


a = [3, 1, 2, 5, 4, 6, 7, 5]
ans = brute(a)
print(ans)
ans1 = better(a)
print(ans1)
