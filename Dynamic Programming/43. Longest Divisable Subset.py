def Subset(arr):
    n = len(arr)
    arr.sort()
    dp = [1] * n
    hash_arr = list(range(n))
    for i in range(n):
        for prev_index in range(i):
            if arr[i] % arr[prev_index] == 0 and 1 + dp[prev_index] > dp[i]:
                dp[i] = 1 + dp[prev_index]
                hash_arr[i] = prev_index

    ans = -1
    last = -1
    for i in range(n):
        if dp[i] > ans:
            ans = dp[i]
            last = i
    result = [arr[last]]
    while hash_arr[last] != last:
        last = hash_arr[last]
        result.append(arr[last])

    return result


if __name__ == "__main__":
    arr = [1, 16, 7, 8, 4]
    ans = Subset(arr)
    print("The longest divisible subset elements are:", ans)
