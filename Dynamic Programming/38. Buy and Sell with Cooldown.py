def Memorization(prices, ind, buy, n, dp):
    if ind >= n:
        return 0
    if dp[ind][buy] != -1:
        return dp[ind][buy]
    profit = 0
    if buy == 0:
        profit = max(
            0 + Memorization(prices, ind + 1, 0, n, dp),
            -prices[ind] + Memorization(prices, ind + 1, 1, n, dp)
        )
    if buy == 1:
        profit = max(
            0 + Memorization(prices, ind + 1, 1, n, dp),
            prices[ind] + Memorization(prices, ind + 2, 0, n, dp)
        )
    dp[ind][buy] = profit
    return profit


if __name__ == "__main__":
    prices = [4, 9, 0, 4, 10]
    n = len(prices)
    dp = [[-1 for _ in range(2)] for _ in range(n)]
    result = Memorization(prices, 0, 0, n, dp)
    print(f"The maximum profit that can be generated is {result}")


