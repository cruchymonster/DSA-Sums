def Memorization(n, c, cuts):
    dp = [[-1] * (c + 1) for _ in range(c + 1)]
    cuts = [0] + cuts + [n]
    cuts.sort()
    def f(i, j):
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        mini = float('inf')
        for ind in range(i, j + 1):
            ans = cuts[j + 1] - cuts[i - 1] + f(i, ind - 1) + f(ind + 1, j)
            mini = min(mini, ans)
        dp[i][j] = mini
        return mini
    return f(1, c)

def Tabulation(n, c, cuts):
    cuts = [0] + cuts + [n]
    cuts.sort()
    dp = [[0] * (c + 2) for _ in range(c + 2)]
    for i in range(c, 0, -1):
        for j in range(1, c + 1):
            if i > j:
                continue
            mini = float('inf')
            for ind in range(i, j + 1):
                ans = cuts[j + 1] - cuts[i - 1] + dp[i][ind - 1] + dp[ind + 1][j]
                mini = min(mini, ans)
            dp[i][j] = mini
    return dp[1][c]

if __name__ == "__main__":
    cuts = [3, 5, 1, 4]
    c = len(cuts)
    n = 7
    print("The minimum cost incurred:", Memorization(n, c, cuts))


