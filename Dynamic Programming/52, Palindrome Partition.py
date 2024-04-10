def check(i, j, s):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def f(i, n, s):
    if i == n:
        return 0
    min_cost = float('inf')
    for j in range(i, n):
        if check(i, j, s):
            cost = 1 + f(j + 1, n, s)
            min_cost = min(min_cost, cost)
    return min_cost

def Memorization(i, n, s, dp):
    if i == n:
        return 0
    if dp[i] != -1:
        return dp[i]
    min_cost = float('inf')
    for j in range(i, n):
        if check(i, j, s):
            cost = 1 + Memorization(j + 1, n, s, dp)
            min_cost = min(min_cost, cost)
    dp[i] = min_cost
    return dp[i]

if __name__ == "__main__":
    str = "BABABCBADCEDE"
    n = len(str)
    partitions = Memorization(0, n, str) - 1
    print("The minimum number of partitions:", partitions)


