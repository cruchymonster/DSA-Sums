import sys

def Memorization(i, j1, j2, n, m, grid, dp):
    if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
        return int(-1e9)
    if i == n - 1:
        if j1 == j2:
            return grid[i][j1]
        else:
            return grid[i][j1] + grid[i][j2]
    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]
    maxi = -sys.maxsize
    for di in range(-1, 2):
        for dj in range(-1, 2):
            ans = 0
            if j1 == j2:
                ans = grid[i][j1] + Memorization(i + 1, j1 + di, j2 + dj, n, m, grid, dp)
            else:
                ans = grid[i][j1] + grid[i][j2] + Memorization(i + 1, j1 + di, j2 + dj, n, m, grid, dp)
            maxi = max(maxi, ans)
    dp[i][j1][j2] = maxi
    return maxi

def Tabulation(n, m, grid):
    dp = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]
    for j1 in range(m):
        for j2 in range(m):
            if j1 == j2:
                dp[n - 1][j1][j2] = grid[n - 1][j1]
            else:
                dp[n - 1][j1][j2] = grid[n - 1][j1] + grid[n - 1][j2]
    for i in range(n - 2, -1, -1):
        for j1 in range(m):
            for j2 in range(m):
                maxi = -sys.maxsize
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ans = 0
                        if j1 == j2:
                            ans = grid[i][j1]
                        else:
                            ans = grid[i][j1] + grid[i][j2]
                        if ((j1 + di < 0 or j1 + di >= m) or (j2 + dj < 0 or j2 + dj >= m)):
                            ans += int(-1e9)
                        else:
                            ans += dp[i + 1][j1 + di][j2 + dj]
                        maxi = max(ans, maxi)
                dp[i][j1][j2] = maxi
    return dp[0][0][m - 1]

def DP(n, m, grid):
    dp = [[[-1 for j in range(m)] for i in range(m)] for k in range(n)]
    return Memorization(0, 0, m - 1, n, m, grid, dp)

def main():
    matrix = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
    n = len(matrix)
    m = len(matrix[0])
    print(DP(n, m, matrix))
