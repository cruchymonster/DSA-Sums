def brute(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    vis = [0] * m
    ans = []
    for i in range(n):
        for j in range(m):
            if arr1[i] == arr2[j] and vis[j] == 0:
                ans.append(arr1[i])
                vis[j] = 1
                break
            if arr2[j] > arr1[i]:
                break
    return ans


def optimal(A, B):
    n = len(A)
    m = len(B)
    ans = []
    i, j = 0, 0
    while (i<n and j < m):
        if A[i]< B[j]:
            i += 1
        elif B[j] < A[i]:
            j += 1
        else:
            ans.append(A[i])
            i += 1
            j += 1
    return ans

arr1 = [1, 2, 3, 3, 4, 5, 6]
arr2 = [3, 5]
ans = brute(arr1, arr2)
print(*ans)
ans = optimal(arr1, arr2)
print(*ans)
