prime = int(1e9 + 7)

def Memorization(s1, s2, ind1, ind2, dp):
    if ind2 < 0:
        return 1
    if ind1 < 0:
        return 0
    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]
    if s1[ind1] == s2[ind2]:
        leaveOne = Memorization(s1, s2, ind1 - 1, ind2 - 1, dp)
        stay = Memorization(s1, s2, ind1 - 1, ind2, dp)
        dp[ind1][ind2] = (leaveOne + stay) % prime
        return dp[ind1][ind2]
    else:
        dp[ind1][ind2] = Memorization(s1, s2, ind1 - 1, ind2, dp)
        return dp[ind1][ind2]

def Tabulation(s1, s2, n, m):
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        dp[0][i] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % prime if s1[i - 1] == s2[j - 1] else dp[i - 1][j]
    return dp[n][m]

def main():
    s1 = "babgbag"
    s2 = "bag"
    dp = [[-1 for j in range(len(s2))] for i in range(len(s1))]
    print("The Count of Distinct Subsequences is", Memorization(s1, s2, len(s1) - 1, len(s2) - 1, dp))
