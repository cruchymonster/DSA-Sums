def Memorization(prices, n, ind, buy, cap, dp):
    if ind == n or cap == 0:
        return 0
    if dp[ind][buy][cap] != -1:
        return dp[ind][buy][cap]
    profit = 0
    if buy == 0:
        profit = max(
            0 + Memorization(prices, n, ind + 1, 0, cap, dp),
            -prices[ind] + Memorization(prices, n, ind + 1, 1, cap, dp)
        )
    if buy == 1:
        profit = max(
            0 + Memorization(prices, n, ind + 1, 1, cap, dp),
            prices[ind] + Memorization(prices, n, ind + 1, 0, cap - 1, dp)
        )
    dp[ind][buy][cap] = profit
    return profit

def Tabulation(prices, n, k):
    dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(n + 1)]
    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            for cap in range(1, k + 1):
                if buy == 0:
                    dp[ind][buy][cap] = max(0 + dp[ind + 1][0][cap],
                                            -prices[ind] + dp[ind + 1][1][cap])
                if buy == 1:
                    dp[ind][buy][cap] = max(0 + dp[ind + 1][1][cap],
                                            prices[ind] + dp[ind + 1][0][cap - 1])
    return dp[0][0][k]

if __name__ == "__main__":
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    n = len(prices)
    k = 2
    dp = [[[(-1) for _ in range(k + 1)] for _ in range(2)] for _ in range(n)]
    result = Memorization(prices, n, 0, 0, k, dp)
    print(f"The maximum profit that can be generated is {result}")


