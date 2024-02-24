import sys


def brute(arr):
    maxi = 0
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            summ = 0
            for k in range(i, j+1):
                summ += arr[k]
            maxi = max(maxi,summ)
    return maxi

def better(arr):
    n = len(arr)
    maxi = -sys.maxsize-1
    for i in range(n):
        summ = 0
        for j in range(i,n):
            summ += arr[j]
            maxi = max(maxi,summ)
    return maxi

def optimal(arr):
    n = len(arr)
    maxi = -sys.maxsize-1
    summ = 0
    for i in range(n):
        summ += arr[i]
        if summ > maxi:
            maxi = summ
        if summ < 0:
            summ = 0
    return maxi


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max1 = brute(arr)
print(max1)
max2 = better(arr)
print(max2)
max3 = optimal(arr)
print(max3)
