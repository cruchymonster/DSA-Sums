def Memorization(ind, target, arr, dp):
    if target == 0:
        return True
    if ind == 0:
        return arr[0] == target
    if dp[ind][target] != -1:
        return dp[ind][target]
    notTaken = Memorization(ind - 1, target, arr, dp)
    taken = False
    if arr[ind] <= target:
        taken = Memorization(ind - 1, target - arr[ind], arr, dp)

    dp[ind][target] = notTaken or taken
    return dp[ind][target]

def Tabulation(arr, n):
    totSum = sum(arr)
    dp = [[False for i in range(totSum + 1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = True
    if arr[0] <= totSum:
        dp[0][arr[0]] = True
    for ind in range(1, n):
        for target in range(1, totSum + 1):
            notTaken = dp[ind - 1][target]
            taken = False
            if arr[ind] <= target:
                taken = dp[ind - 1][target - arr[ind]]
            dp[ind][target] = notTaken or taken
    mini = int(1e9)
    for i in range(totSum + 1):
        if dp[n - 1][i] == True:
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)
    return mini

def Iteration(arr):
    n = len(arr)
    totSum = sum(arr)
    dp = [[-1 for i in range(totSum + 1)] for j in range(n)]
    for i in range(totSum + 1):
        dummy = Memorization(n - 1, i, arr, dp)
    mini = int(1e9)
    for i in range(totSum + 1):
        if dp[n - 1][i] == True:
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)
    return mini

def main():
    arr = [1, 2, 3, 4]
    print("The minimum absolute difference is:", Iteration(arr))
