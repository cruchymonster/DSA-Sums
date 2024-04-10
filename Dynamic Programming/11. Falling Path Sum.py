import sys

def Memorization(i, j, m, matrix, dp):
    if j < 0 or j >= m:
        return -int(1e9)
    if i == 0:
        return matrix[0][j]
    if dp[i][j] != -1:
        return dp[i][j]
    up = matrix[i][j] + Memorization(i - 1, j, m, matrix, dp)
    leftDiagonal = matrix[i][j] + Memorization(i - 1, j - 1, m, matrix, dp)
    rightDiagonal = matrix[i][j] + Memorization(i - 1, j + 1, m, matrix, dp)
    dp[i][j] = max(up, max(leftDiagonal, rightDiagonal))
    return dp[i][j]

def Tabulation(matrix):
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0 for j in range(m)] for i in range(n)]
    for j in range(m):
        dp[0][j] = matrix[0][j]
    for i in range(1, n):
        for j in range(m):
            up = matrix[i][j] + dp[i - 1][j]
            left_diagonal = matrix[i][j]
            if j - 1 >= 0:
                left_diagonal += dp[i - 1][j - 1]
            else:
                left_diagonal += -int(1e9)
            right_diagonal = matrix[i][j]
            if j + 1 < m:
                right_diagonal += dp[i - 1][j + 1]
            else:
                right_diagonal += -int(1e9)
            dp[i][j] = max(up, left_diagonal, right_diagonal)
    maxi = -sys.maxsize
    for j in range(m):
        maxi = max(maxi, dp[n - 1][j])
    return maxi

def getMaxPathSum():
    matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
    n = len(matrix)
    m = len(matrix[0])
    dp = [[-1 for j in range(m)] for i in range(n)]
    maxi = -sys.maxsize
    for j in range(m):
        ans = Memorization(n - 1, j, m, matrix, dp)
        maxi = max(maxi, ans)
    print(maxi)
