def Memorization(i, j, triangle, n, dp):
    if dp[i][j] != -1:
        return dp[i][j]
    if i == n - 1:
        return triangle[i][j]
    down = triangle[i][j] + Memorization(i + 1, j, triangle, n, dp)
    diagonal = triangle[i][j] + Memorization(i + 1, j + 1, triangle, n, dp)
    dp[i][j] = min(down, diagonal)
    return dp[i][j]

def Tabulization(triangle, n):
    dp = [[0 for j in range(n)] for i in range(n)]
    for j in range(n):
        dp[n - 1][j] = triangle[n - 1][j]
    for i in range(n - 2, -1, -1):
        for j in range(i, -1, -1):
            down = triangle[i][j] + dp[i + 1][j]
            diagonal = triangle[i][j] + dp[i + 1][j + 1]
            dp[i][j] = min(down, diagonal)
    return dp[0][0]

def main():
    triangle = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]]
    n = len(triangle)
    dp = [[-1 for j in range(n)] for i in range(n)]
    print(Memorization(0, 0, triangle, n, dp))
