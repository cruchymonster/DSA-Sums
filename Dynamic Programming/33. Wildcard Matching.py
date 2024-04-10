def Check(S1, i):
    for j in range(i + 1):
        if S1[j] != '*':
            return False
    return True

def Memorization(S1, S2, i, j, dp):
    if i < 0 and j < 0:
        return True
    if i < 0 and j >= 0:
        return False
    if j < 0 and i >= 0:
        return Check(S1, i)
    if dp[i][j] != -1:
        return dp[i][j]

    if S1[i] == S2[j] or S1[i] == '?':
        dp[i][j] = Memorization(S1, S2, i - 1, j - 1, dp)
    elif S1[i] == '*':
        dp[i][j] = Memorization(S1, S2, i - 1, j, dp) or Memorization(S1, S2, i, j - 1, dp)
    else:
        dp[i][j] = False
    return dp[i][j]

def main():
    S1 = "ab*cd"
    S2 = "abdefcd"
    n = len(S1)
    m = len(S2)
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    if Memorization(S1, S2, n - 1, m - 1, dp):
        print("String S1 and S2 do match")
    else:
        print("String S1 and S2 do not match")
