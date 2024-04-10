def memorization(day, last, points, dp):
    if dp[day][last] != -1:
        return dp[day][last]
    if day == 0:
        maxi = 0
        for i in range(3):
            if i != last:
                maxi = max(maxi, points[0][i])
        dp[day][last] = maxi
        return dp[day][last]
    maxi = 0
    for i in range(3):
        if i != last:
            activity = points[day][i] + memorization(day - 1, i, points, dp)
            maxi = max(maxi, activity)
    dp[day][last] = maxi
    return dp[day][last]

def Tabulation(n, points):
    dp = [[0 for j in range(4)] for i in range(n)]
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], max(points[0][1], points[0][2]))
    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    activity = points[day][task] + dp[day - 1][task]
                    dp[day][last] = max(dp[day][last], activity)
    return dp[n - 1][3]

def main():
    points = [[10, 40, 70],
              [20, 50, 80],
              [30, 60, 90]]
    n = len(points)
    dp = [[-1 for j in range(4)] for i in range(n)]
    print(memorization(n - 1, 3, points, dp))
