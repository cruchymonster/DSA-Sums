def brute(arr):
    n = len(arr)
    pos = []
    neg = []
    for i in range(n):
        if arr[i] > 0:
            pos.append(arr[i])
        else:
            neg.append((arr[i]))
    for i in range(len(pos)):
        arr[2*i] = pos[i]
    for i in range(len(neg)):
        arr[2*i+1] = neg[i]
    return arr

def optimal(arr):
    n = len(arr)
    ans = [0] * n
    pos,neg = 0,1
    for i in range(n):
        if arr[i] < 0:
            ans[neg] = arr[i]
            neg += 2
        else:
            ans[pos] = arr[i]
            pos += 2
    return ans


nums = [1, 2, -4, -5]
num = brute(nums)
print(num)
num1 = optimal(nums)
print(num1)
