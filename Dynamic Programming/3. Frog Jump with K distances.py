import sys

def memorization(ind, height, dp, k):
    if ind == 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]
    mmSteps = sys.maxsize
    for j in range(1, k + 1):
        if ind - j >= 0:
            jump = memorization(ind - j, height, dp, k) + abs(height[ind] - height[ind - j])
            mmSteps = min(jump, mmSteps)
    dp[ind] = mmSteps
    return dp[ind]

def Tabulization(n, height, dp, k):
    dp[0] = 0
    for i in range(1, n):
        mmSteps = sys.maxsize
        for j in range(1, k+1):
            if i - j >= 0:
                jump = dp[i - j] + abs(height[i] - height[i - j])
                mmSteps = min(jump, mmSteps)
        dp[i] = mmSteps
    return dp[n-1]

height = [30, 10, 60, 10, 60, 50]
n = len(height)
k = 2
dp = [-1] * n
print(memorization(n-1, height, dp, k))
