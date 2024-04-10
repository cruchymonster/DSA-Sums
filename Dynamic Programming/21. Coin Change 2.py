def Memorization(arr, ind, T, dp):
    if ind == 0:
        return 1 if T % arr[0] == 0 else 0
    if dp[ind][T] != -1:
        return dp[ind][T]
    not_taken = Memorization(arr, ind - 1, T, dp)
    taken = 0
    if arr[ind] <= T:
        taken = Memorization(arr, ind, T - arr[ind], dp)
    dp[ind][T] = not_taken + taken
    return dp[ind][T]

def Tabulation(arr, n, T):
    dp = [[0 for j in range(T + 1)] for i in range(n)]
    for i in range(T + 1):
        if i % arr[0] == 0:
            dp[0][i] = 1
    for ind in range(1, n):
        for target in range(T + 1):
            notTaken = dp[ind - 1][target]
            taken = 0
            if arr[ind] <= target:
                taken = dp[ind][target - arr[ind]]
            dp[ind][target] = notTaken + taken
    return dp[n - 1][T]

def main():
    arr = [1, 2, 3]
    T = 4
    n = len(arr)
    dp = [[-1 for i in range(T + 1)] for j in range(n)]
    print("The total number of ways is", Memorization(arr, n - 1, T, dp))
