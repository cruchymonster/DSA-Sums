def f(arr):
    N = len(arr)
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
    for i in range(N - 1, 0, -1):
        for j in range(i + 1, N):
            mini = float('inf')
            for k in range(i, j):
                ans = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                mini = min(mini, ans)
            dp[i][j] = mini
    return dp[1][N - 1]


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print("The minimum number of operations is:", f(arr))
