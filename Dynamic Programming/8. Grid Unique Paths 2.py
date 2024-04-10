def Memorization(i, j, maze, dp):
    if i < 0 or j < 0 or maze[i][j] == -1:
        return 0
    if i == 0 and j == 0:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    up = Memorization(i - 1, j, maze, dp)
    left = Memorization(i, j - 1, maze, dp)
    dp[i][j] = up + left
    return dp[i][j]

def Tabulation(n, m, maze, dp):
    for i in range(n):
        for j in range(m):
            if i > 0 and j > 0 and maze[i][j] == -1:
                dp[i][j] = 0
                continue
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            up = 0
            left = 0
            if i > 0:
                up = dp[i - 1][j]
            if j > 0:
                left = dp[i][j - 1]
            dp[i][j] = up + left
    return dp[n - 1][m - 1]

def main():
    maze = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]
    n = len(maze)
    m = len(maze[0])
    dp = [[-1 for j in range(m)] for i in range(n)]
    print(Memorization(n - 1, m - 1, maze, dp))
