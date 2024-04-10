def Memorization(num, k):
    n = len(num)
    dp = [-1] * n
    def f(ind):
        if ind == n:
            return 0
        if dp[ind] != -1:
            return dp[ind]
        len_val = 0
        max_val = float('-inf')
        max_ans = float('-inf')
        for j in range(ind, min(ind + k, n)):
            len_val += 1
            max_val = max(max_val, num[j])
            summation = len_val * max_val + f(j + 1)
            max_ans = max(max_ans, summation)
        dp[ind] = max_ans
        return dp[ind]
    return f(0)

def Tabulation(num, k):
    n = len(num)
    dp = [0] * (n + 1)

    for ind in range(n - 1, -1, -1):
        len_val = 0
        max_val = float('-inf')
        max_ans = float('-inf')
        for j in range(ind, min(ind + k, n)):
            len_val += 1
            max_val = max(max_val, num[j])
            summation = len_val * max_val + dp[j + 1]
            max_ans = max(max_ans, summation)
        dp[ind] = max_ans
    return dp[0]

if __name__ == "__main__":
    num = [1, 15, 7, 9, 2, 5, 10]
    k = 3
    max_sum = Memorization(num, k)
    print("The maximum sum is:", max_sum)


