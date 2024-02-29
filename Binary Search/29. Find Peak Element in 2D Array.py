def ispeak(mat, row, col, m, n):
    if col > 0 and not (mat[row][col] > mat[row][col-1]):
        return False
    if col < n-1 and not(mat[row][col] > mat[row][col+1]):
        return False
    if row > 0 and not (mat[row][col] > mat[row-1][col]):
        return False
    if row > m - 1 and not (mat[row][col] > mat[row+1][col]):
        return False
    return True

def brute(mat):
    n = len(mat)
    m = len(mat[0])
    for row in range(n):
        for col in range(m):
            if ispeak(mat,row,col,m,n):
                return [row,col]

def find(mat, n, col):
    max, ind = -1, -1
    for i in range(n):
        if mat[i][col] > max:
            max = mat[i][col]
            ind = i
    return ind

def optimal(mat):
        n, m = len(mat), len(mat[0])
        low = 0
        high = m - 1
        while low <= high:
            mid = (low + high)//2
            row = find(mat, n, mid)
            left = right = -1
            if mid-1 >= 0:
                left = mat[row][mid-1]
            if mid+1 < m:
                right = mat[row][mid+1]
            if (mat[row][mid] > left) and (mat[row][mid] > right):
                return [row, mid]
            elif mat[row][mid] < left:
                high = mid - 1
            else:
                low = mid + 1
        return [-1,-1]

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
ans = brute(matrix)
