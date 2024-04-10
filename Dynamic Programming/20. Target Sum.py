def Memorization(ind, target, arr, dp):
    if ind == 0:
        if target == 0 and arr[0] == 0:
            return 2
        if target == 0 or target == arr[0]:
            return 1
        return 0
    if dp[ind][target] != -1:
        return dp[ind][target]
    notTaken = Memorization(ind - 1, target, arr, dp)
    taken = 0
    if arr[ind] <= target:
        taken = Memorization(ind - 1, target - arr[ind], arr, dp)
    dp[ind][target] = notTaken + taken
    return dp[ind][target]

def targetSum(n, target, arr):
    totSum = 0
    for i in range(len(arr)):
        totSum += arr[i]
    if totSum - target < 0:
        return 0
    if (totSum - target) % 2 == 1:
        return 0
    s2 = (totSum - target) // 2
    dp = [[-1 for j in range(s2 + 1)] for i in range(n)]
    return Memorization(n - 1, s2, arr, dp)

def main():
    arr = [1, 2, 3, 1]
    target = 3
    n = len(arr)
    print("The number of ways found is", targetSum(n, target, arr))
