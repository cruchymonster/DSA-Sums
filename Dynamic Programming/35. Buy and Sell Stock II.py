def f(Arr, n):
    if n == 0:
        return 0
    dp = [[-1 for _ in range(2)] for _ in range(n)]
    def Memorization(ind, buy):
        if ind == n:
            return 0

        if dp[ind][buy] != -1:
            return dp[ind][buy]
        profit = 0
        if buy == 0:
            profit = max(0 + Memorization(ind + 1, 0), -Arr[ind] + Memorization(ind + 1, 1))
        elif buy == 1:
            profit = max(0 + Memorization(ind + 1, 1), Arr[ind] + Memorization(ind + 1, 0))
        dp[ind][buy] = profit
        return profit
    ans = Memorization(0, 0)
    return ans

def Tabulation(Arr, n):
    dp = [[-1 for _ in range(2)] for _ in range(n + 1)]
    dp[n][0] = dp[n][1] = 0
    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            profit = 0
            if buy == 0:
                profit = max(0 + dp[ind + 1][0], -Arr[ind] + dp[ind + 1][1])
            elif buy == 1:
                profit = max(0 + dp[ind + 1][1], Arr[ind] + dp[ind + 1][0])
            dp[ind][buy] = profit
    return dp[0][0]

def main():
    n = 6
    Arr = [7, 1, 5, 3, 6, 4]

    max_profit = f(Arr, n)
    print("The maximum profit that can be generated is", max_profit)

if __name__ == "__main__":
    main()


