def linear(a, num):
    n = len(a)  # size of array
    for i in range(n):
        if a[i] == num:
            return True
    return False

def brute(a):
    n = len(a)
    longest = 1
    for i in range(n):
        x = a[i]
        cnt = 1
        while linear(a, x + 1):
            x += 1
            cnt += 1

        longest = max(longest, cnt)
    return longest

def better(a):
    n = len(a)
    if n==0:
        return 0
    a.sort()
    lastsmaller = 0
    cnt = 0
    longest = 0
    for i in range(n):
        if a[i] - 1 == lastsmaller:
            cnt += 1
            lastsmaller = a[i]
        elif a[i] != lastsmaller:
            cnt = 1
            lastsmaller = a[i]
        longest = max(longest, cnt)
    return longest

def optimal(a):
    n = len(a)
    longest = 1
    st = set()
    for i in range(n):
        st.add(a[i])
    for it in st:
        if it - 1 in st:
            cnt = 1
            x = it
            while x + 1 in st:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest


a = [100, 200, 1, 2, 3, 4]
ans = brute(a)
print(ans)
ans1 = better(a)
print(ans1)
