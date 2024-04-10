import sys
import math

def memorization(ind, height, dp):
    if ind == 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]
    jumpTwo = sys.maxsize
    jumpOne = memorization(ind-1, height, dp) + abs(height[ind] - height[ind-1])
    if ind > 1:
        jumpTwo = memorization(ind-2, height, dp) + abs(height[ind] - height[ind-2])
    dp[ind] = min(jumpOne, jumpTwo)
    return dp[ind]

def tabulization(height, n, dp):
    dp[0] = 0
    for ind in range(1, n):
        jumpTwo = float('inf')
        jumpOne = dp[ind-1] + abs(height[ind]-height[ind-1])
        if ind > 1:
            jumpTwo = dp[ind-2] + abs(height[ind]-height[ind-2])
        dp[ind] = min(jumpOne, jumpTwo)
    print(dp[n-1])


height = [30, 10, 60, 10, 60, 50]
n = len(height)
dp = [-1] * n
print(memorization(n-1, height, dp))

