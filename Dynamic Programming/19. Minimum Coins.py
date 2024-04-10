def Memorization(arr, ind, T, dp):
    if ind == 0:
        if T % arr[0] == 0:
            return T // arr[0]
        else:
            return int(1e9)
    if dp[ind][T] != -1:
        return dp[ind][T]
    notTaken = 0 + Memorization(arr, ind - 1, T, dp)
    taken = int(1e9)
    if arr[ind] <= T:
        taken = 1 + Memorization(arr, ind, T - arr[ind], dp)
    dp[ind][T] = min(notTaken, taken)
    return dp[ind][T]

def Tabulation(arr, T):
    n = len(arr)
    dp = [[0 for _ in range(T + 1)] for _ in range(n)]
    for i in range(T + 1):
        if i % arr[0] == 0:
            dp[0][i] = i // arr[0]
        else:
            dp[0][i] = int(1e9)
    for ind in range(1, n):
        for target in range(T + 1):
            notTake = dp[ind - 1][target]
            take = int(1e9)
            if arr[ind] <= target:
                take = 1 + dp[ind][target - arr[ind]]
            dp[ind][target] = min(notTake, take)
    ans = dp[n - 1][T]
    if ans >= int(1e9):
        return -1
    return ans

def main():
    arr = [1, 2, 3]
    T = 7
    n = len(arr)
    dp = [[-1 for j in range(T + 1)] for i in range(n)]
    ans = Memorization(arr, n - 1, T, dp)
    if ans >= int(1e9):
        return -1
    return ans
