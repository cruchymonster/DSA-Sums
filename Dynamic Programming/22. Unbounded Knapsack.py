import sys

def Memorization(wt, val, ind, W, dp):
    if ind == 0:
        return (W // wt[0]) * val[0]
    if dp[ind][W] != -1:
        return dp[ind][W]
    notTaken = Memorization(wt, val, ind - 1, W, dp)
    taken = -sys.maxsize
    if wt[ind] <= W:
        taken = val[ind] + Memorization(wt, val, ind, W - wt[ind], dp)
    dp[ind][W] = max(notTaken, taken)
    return dp[ind][W]

def Tabulation(n, W, val, wt):
    dp = [[0 for j in range(W + 1)] for i in range(n)]
    for i in range(wt[0], W + 1, wt[0]):
        dp[0][i] = ((i // wt[0]) * val[0])
    for ind in range(1, n):
        for cap in range(W + 1):
            notTaken = 0 + dp[ind - 1][cap]
            taken = -sys.maxsize
            if wt[ind] <= cap:
                taken = val[ind] + dp[ind][cap - wt[ind]]
            dp[ind][cap] = max(notTaken, taken)
    return dp[n - 1][W]

def main():
    wt = [2, 4, 6]
    val = [5, 11, 13]
    W = 10
    n = len(wt)
    dp = [[-1 for _ in range(W + 1)] for _ in range(n)]
    print("The Maximum value of items the thief can steal is", Memorization(wt, val, n - 1, W, dp))
