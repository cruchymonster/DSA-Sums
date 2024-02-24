def brute(arr):
    n = len(arr)
    for i in range(n):
        num = arr[i]
        cnt = 0
        for j in range(n):
            if arr[j] == num:
                cnt += 1
        if cnt == 1:
            return num

def optimal(arr):
    xor = 0
    for num in arr:
        xor ^= num
    return xor


arr = [4, 1, 2, 1, 2]
ans = brute(arr)
print(ans)
a = optimal(arr)
print(a)
