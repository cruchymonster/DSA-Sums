def brute(arr):
    maxi = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                maxi = max(maxi, arr[j]-arr[i])
    return maxi

def optimal(arr):
    n = len(arr)
    maxi = 0
    mini = float('inf')
    for i in range(n):
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i] - mini)
    return maxi


arr = [7, 1, 5, 3, 6, 4]
max1 = brute(arr)
print(max1)
max2 = optimal(arr)
print(max2)
