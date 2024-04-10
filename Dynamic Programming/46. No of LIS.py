def Count(arr):
    n = len(arr)
    dp = [1] * n
    count = [1] * n
    maxi = 1
    for i in range(n):
        for prev in range(i):
            if arr[prev] < arr[i] and dp[prev] + 1 > dp[i]:
                dp[i] = dp[prev] + 1
                count[i] = count[prev]
            elif arr[prev] < arr[i] and dp[prev] + 1 == dp[i]:
                count[i] += count[prev]
        maxi = max(maxi, dp[i])

    num_of_LIS = 0
    for i in range(n):
        if dp[i] == maxi:
            num_of_LIS += count[i]

    return num_of_LIS


if __name__ == "__main__":
    arr = [1, 5, 4, 3, 2, 6, 7, 2]

    print("The count of Longest Increasing Subsequences is:", Count(arr))
