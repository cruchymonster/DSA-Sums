def PrintLIC(arr, n):
    dp = [1] * n
    hash = [i for i in range(n)]
    for i in range(n):
        hash[i] = i
        for prev in range(i):
            if arr[prev] < arr[i] and 1 + dp[prev] > dp[i]:
                dp[i] = 1 + dp[prev]
                hash[i] = prev
    ans = -1
    Last = -1
    for i in range(n):
        if dp[i] > ans:
            ans = dp[i]
            Last = i
    temp = [arr[Last]]
    while hash[Last] != Last:
        Last = hash[Last]
        temp.append(arr[Last])
    temp.reverse()
    for i in range(len(temp)):
        print(temp[i])
    print()
    return ans

arr = [10, 9, 2, 5, 3, 7, 101, 18]
n = len(arr)
print("Length of the longest increasing subsequence:", PrintLIC(arr, n))
