def maxProfit(prices):
    n = len(prices)
    dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]

    def Memorization(ind, buy, cap):
        if ind == n or cap == 0:
            return 0
        if dp[ind][buy][cap] != -1:
            return dp[ind][buy][cap]
        profit = 0
        if buy == 0:
            profit = max(0 + Memorization(ind + 1, 0, cap), -prices[ind] + Memorization(ind + 1, 1, cap))
        elif buy == 1:
            profit = max(0 + Memorization(ind + 1, 1, cap), prices[ind] + Memorization(ind + 1, 0, cap - 1))
        dp[ind][buy][cap] = profit
        return profit
    return Memorization(0, 0, 2)

def Tabulation(prices):
    n = len(prices)
    dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            for cap in range(1, 3):
                if buy == 0:
                    dp[ind][buy][cap] = max(0 + dp[ind + 1][0][cap], -prices[ind] + dp[ind + 1][1][cap])
                elif buy == 1:
                    dp[ind][buy][cap] = max(0 + dp[ind + 1][1][cap], prices[ind] + dp[ind + 1][0][cap - 1])
    return dp[0][0][2]

def main():
    prices = [3, 3, 5, 0, 0, 3, 1, 4]

    max_profit = maxProfit(prices)
    print("The maximum profit that can be generated is", max_profit)

if __name__ == "__main__":
    main()


