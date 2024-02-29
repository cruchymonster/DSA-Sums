def brute(array1, array2, m, n, k):
    p1 = 0
    p2 = 0
    cnt = 0
    answer = 0
    while (p1 < m and p2 < n):
        if (cnt == k):
            break
        elif (array1[p1] < array2[p2]):
            answer = array1[p1]
            p1 += 1
        else:
            answer = array2[p2]
            p2 += 1
        cnt += 1
    if (cnt != k):
        if (p1 != m-1):
            answer = array1[k-cnt]
        else:
            answer = array2[k-cnt]
    return answer

def optimal(nums1, nums2, m, n, k):
    if m > n:
        return optimal(nums2, nums1, n, m, k)
    low = max(0, k-m)
    high = min(k, n)
    while low <= high:
        cut1 = (low+high)//2
        cut2 = k - cut1
        l1 = float('-inf') if cut1 == 0 else nums1[cut1-1]
        l2 = float('-inf') if cut2 == 0 else nums2[cut2-1]
        r1 = float('inf') if cut1 == m else nums1[cut1]
        r2 = float('inf') if cut2 == n else nums2[cut2]
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = cut1-1
        else:
            low = cut1+1
    return 1

array1 = [2, 3, 6, 7, 9]
array2 = [1, 4, 8, 10]
m = len(array1)
n = len(array2)
k = 5
ans = brute(array1, array2, m, n, k)
