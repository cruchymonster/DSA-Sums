def Memorization(prices, ind, buy, n, fee, dp):
    if ind == n:
        return 0
    if dp[ind][buy] != -1:
        return dp[ind][buy]
    profit = 0
    if buy == 0:
        profit = max(
            0 + Memorization(prices, ind + 1, 0, n, fee, dp),
            -prices[ind] + Memorization(prices, ind + 1, 1, n, fee, dp)
        )
    if buy == 1:
        profit = max(
            0 + Memorization(prices, ind + 1, 1, n, fee, dp),
            prices[ind] - fee + Memorization(prices, ind + 1, 0, n, fee, dp)
        )
    dp[ind][buy] = profit
    return profit

def Tabulation(n, fee, prices):
    if n == 0:
        return 0
    dp = [[0 for _ in range(2)] for _ in range(n + 1)]
    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            profit = 0
            if buy == 0:
                profit = max(
                    0 + dp[ind + 1][0],
                    -prices[ind] + dp[ind + 1][1]
                )
            if buy == 1:
                profit = max(
                    0 + dp[ind + 1][1],
                    prices[ind] - fee + dp[ind + 1][0]
                )
            dp[ind][buy] = profit
    return dp[0][0]


if __name__ == "__main__":
    prices = [1, 3, 2, 8, 4, 9]
    n = len(prices)
    fee = 2
    dp = [[-1 for _ in range(2)] for _ in range(n)]
    result = Memorization(prices, 0, 0, n, fee, dp)
    print(f"The maximum profit that can be generated is {result}")


