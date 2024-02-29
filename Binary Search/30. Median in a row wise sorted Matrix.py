def brute(arr, n, m):
    median = [0] * (n * m)
    ind = 0
    for i in range(n):
        for j in range(m):
            median[ind] = arr[i][j]
            ind += 1
    return median[(n * m) // 2]

def optimal(m, r, d):
    mi = m[0][0]
    mx = 0
    for i in range(r):
        if m[i][0] < mi:
            mi = m[i][0]
        if m[i][d-1] > mx :
            mx =  m[i][d-1]
    desired = (r * d + 1) // 2
    while (mi < mx):
        mid = mi + (mx - mi) // 2
        place = [0];
        for i in range(r):
             j = max(m[i], mid)
             place[0] = place[0] + j
        if place[0] < desired:
            mi = mid + 1
        else:
            mx = mid
    print ("Median is", mi)
    return

arr = [[1,3,8], [2, 3, 4], [1, 2, 5]]
n = 3
m = 3
ans = brute(arr, n, m)
print(ans)
