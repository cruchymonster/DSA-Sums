mod =int(1e9+7)

def findWays(num, tar):
    n = len(num)
    prev = [0] * (tar + 1)
    if num[0] == 0:
        prev[0] = 2
    else:
        prev[0] = 1
    if num[0] != 0 and num[0] <= tar:
        prev[num[0]] = 1
    for ind in range(1, n):
        cur = [0] * (tar + 1)
        for target in range(tar + 1):
            notTaken = prev[target]
            taken = 0
            if num[ind] <= target:
                taken = prev[target - num[ind]]
            cur[target] = (notTaken + taken) % mod
        prev = cur
    return prev[tar]

def countPartitions(n, d, arr):
    totSum = 0
    for i in range(n):
        totSum += arr[i]
    if totSum - d < 0 or (totSum - d) % 2:
        return 0
    return findWays(arr, (totSum - d) // 2)

def main():
    arr = [5, 2, 6, 4]
    n = len(arr)
    d = 3
    print("The number of subsets found are", countPartitions(n, d, arr))
