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

def Tabulation(n, arr):
    totSum = sum(arr)
    if totSum % 2 == 1:
        return False
    else:
        k = totSum // 2
        dp = [[False for j in range(k + 1)] for i in range(n)]
        for i in range(n):
            dp[i][0] = True
        if arr[0] <= k:
            dp[0][arr[0]] = True
        for ind in range(1, n):
            for target in range(1, k + 1):
                notTaken = dp[ind - 1][target]
                taken = False
                if arr[ind] <= target:
                    taken = dp[ind - 1][target - arr[ind]]
                dp[ind][target] = notTaken or taken
        return dp[n - 1][k]

def main():
    arr = [2, 3, 3, 3, 4, 5]
    n = len(arr)
    totSum = sum(arr)
    if totSum % 2 == 1:
        return False
    else:
        k = totSum // 2
        dp = [[-1 for i in range(k + 1)] for j in range(n)]
        if Memorization(n - 1, k, arr, dp):
            print("The Array can be partitioned into two equal subsets")
        else:
            print("The Array cannot be partitioned into two equal subsets")
