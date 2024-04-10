def Bitonic(arr):
    n = len(arr)
    dp1 = [1] * n
    dp2 = [1] * n
    for i in range(n):
        for prev in range(i):
            if arr[prev] < arr[i]:
                dp1[i] = max(dp1[i], 1 + dp1[prev])
    for i in range(n - 1, -1, -1):
        for prev in range(n - 1, i, -1):
            if arr[prev] < arr[i]:
                dp2[i] = max(dp2[i], 1 + dp2[prev])
    maxi = -1
    for i in range(n):
        maxi = max(maxi, dp1[i] + dp2[i] - 1)
    return maxi


if __name__ == "__main__":
    arr = [1, 11, 2, 10, 4, 5, 2, 1]
    n = len(arr)

    print("The length of the longest bitonic subsequence is", Bitonic(arr))
