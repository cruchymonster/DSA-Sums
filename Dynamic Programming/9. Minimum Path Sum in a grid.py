def Memorization(i, j, matrix, dp):
    if i == 0 and j == 0:
        return matrix[0][0]
    if i < 0 or j < 0:
        return int(1e9)
    if dp[i][j] != -1:
        return dp[i][j]
    up = matrix[i][j] + Memorization(i - 1, j, matrix, dp)
    left = matrix[i][j] + Memorization(i, j - 1, matrix, dp)
    dp[i][j] = min(up, left)
    return dp[i][j]

def Tabulation(n, m, matrix):
    dp = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = matrix[i][j]
            else:
                up = matrix[i][j]
                if i > 0:
                    up += dp[i-1][j]
                else:
                    up += int(1e9)
                left = matrix[i][j]
                if j > 0:
                    left += dp[i][j-1]
                else:
                    left += int(1e9)
                dp[i][j] = min(up, left)
    return dp[n-1][m-1]

def main():
    matrix = [[5, 9, 6],
              [11, 5, 2]]
    n = len(matrix)
    m = len(matrix[0])
    dp = [[-1 for j in range(m)] for i in range(n)]
    print(Memorization(n - 1, m - 1, matrix, dp))
