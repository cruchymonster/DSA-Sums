def Memorization(S1, S2, i, j, dp):
    # Base cases
    if i < 0:
        return j + 1
    if j < 0:
        return i + 1
    if dp[i][j] != -1:
        return dp[i][j]
    if S1[i] == S2[j]:
        dp[i][j] = Memorization(S1, S2, i - 1, j - 1, dp)
    else:
        dp[i][j] = 1 + min(
            Memorization(S1, S2, i - 1, j - 1, dp),
            min(Memorization(S1, S2, i - 1, j, dp), Memorization(S1, S2, i, j - 1, dp)))
    return dp[i][j]

def Tabulation(S1, S2):
    n = len(S1)
    m = len(S2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1]))
    return dp[n][m]

def main():
    s1 = "horse"
    s2 = "ros"
    n = len(s1)
    m = len(s2)
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    print("The minimum number of operations required is:", Memorization(s1, s2, n - 1, m - 1, dp))
