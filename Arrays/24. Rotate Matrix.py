def brute(matrix):
    n = len(matrix)
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = matrix[i][j]
    return rotated

def optimal(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated = brute(arr)
for i in range(len(rotated)):
    for j in range(len(rotated[0])):
        print(rotated[i][j], end=" ")
    print()
optimal(arr)
print()
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end=" ")
    print()
