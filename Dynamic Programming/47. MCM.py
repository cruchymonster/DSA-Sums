def f(arr, i, j, dp):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    mini = float('inf')
    for k in range(i, j):
        ans = f(arr, i, k, dp) + f(arr, k+1, j, dp) + arr[i-1] * arr[k] * arr[j]
        mini = min(mini, ans)

    dp[i][j] = mini
    return mini

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    N = len(arr)
    dp = [[-1] * N for _ in range(N)]
    i = 1
    j = N - 1
    print("The minimum number of operations is", f(arr, i, j, dp))
