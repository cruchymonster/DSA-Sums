def Memorization(arr, n, ind, prev_index, dp):
    if ind == n:
        return 0
    if dp[ind][prev_index + 1] != -1:
        return dp[ind][prev_index + 1]
    not_take = 0 + Memorization(arr, n, ind + 1, prev_index, dp)
    take = 0
    if prev_index == -1 or arr[ind] > arr[prev_index]:
        take = 1 + Memorization(arr, n, ind + 1, ind, dp)

    dp[ind][prev_index + 1] = max(not_take, take)
    return dp[ind][prev_index + 1]

def Tabulation(arr, n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for ind in range(n - 1, -1, -1):
        for prev in range(ind - 1, -2, -1):
            notTake = 0 + dp[ind + 1][prev + 1]
            take = 0
            if prev == -1 or arr[ind] > arr[prev]:
                take = 1 + dp[ind + 1][ind + 1]
            dp[ind][prev + 1] = max(notTake, take)

    return dp[0][0]

if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    n = len(arr)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
    result = Memorization(arr, n, 0, -1, dp)
    print("The length of the longest increasing subsequence is", result)
