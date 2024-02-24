def markrow(a, n, m, i):
    for j in range(m):
        if a[i][j] != 0:
            a[i][j] = -1

def markcol(a, n, m, j):
    for i in range(n):
        if a [i][j] != 0:
            a[i][j] = -1

def brute(a, n, m):
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                markrow(a,n,m,i)
                markcol(a,n,m,j)
    for i in range(n):
        for j in range(m):
            if a[i][j] == -1:
                a[i][j] = 0
    return a


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
n = len(matrix)
m = len(matrix[0])
ans = brute(matrix, n, m)
for row in ans:
    for ele in row:
        print(ele, end="")
    print()
