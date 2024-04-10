def memorization(ind, arr, dp):
    if dp[ind] != -1:
        return dp[ind]
    if ind == 0:
        return arr[ind]
    if ind < 0:
        return 0
    pick = arr[ind] + memorization(ind - 2, arr, dp)
    nonPick = 0 + memorization(ind - 1, arr, dp)
    dp[ind] = max(pick, nonPick)
    return dp[ind]

def Tabulization(n, arr, dp):
    dp[0] = arr[0]
    for i in range(1, n):
        pick = arr[i]
        if i > 1:
            pick += dp[i - 2]
        non_pick = 0 + dp[i - 1]
        dp[i] = max(pick, non_pick)
    return dp[n - 1]

arr = [2, 1, 4, 9]
n = len(arr)
dp = [-1 for i in range(n)]
print(memorization(n - 1, arr, dp))
