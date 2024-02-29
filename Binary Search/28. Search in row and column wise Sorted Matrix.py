def brute(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target:
                return True
    return False

def binarySearch(nums, target):
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False

def better(matrix, target):
    n = len(matrix)
    for i in range(n):
        flag = binarySearch(matrix[i], target)
        if flag:
            return True
    return False

def optimal(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    row = 0
    col = m - 1
    while row < n and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
result = brute(matrix, 8)
