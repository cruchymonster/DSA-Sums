def Memorization(num, k):
    n = len(num)
    dp = [[0] * (k + 1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    if num[0] <= k:
        dp[0][num[0]] = 1
    for ind in range(1, n):
        for target in range(1, k + 1):
            notTaken = dp[ind - 1][target]
            taken = 0
            if num[ind] <= target:
                taken = dp[ind - 1][target - num[ind]]
            dp[ind][target] = notTaken + taken
    return dp[n - 1][k]

def Tabulation(num, k):
    n = len(num)
    dp = [[0] * (k + 1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    if num[0] <= k:
        dp[0][num[0]] = 1
    for ind in range(1, n):
        for target in range(1, k + 1):
            notTaken = dp[ind - 1][target]
            taken = 0
            if num[ind] <= target:
                taken = dp[ind - 1][target - num[ind]]
            dp[ind][target] = notTaken + taken
    return dp[n - 1][k]

def main():
    arr = [1, 2, 2, 3]
    k = 3
    print("The number of subsets found are", Memorization(arr, k))
