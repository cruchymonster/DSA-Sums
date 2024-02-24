def brute(arr, key):
    n = len(arr)
    st = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    sum = arr[i] + arr[j] + arr[k] + arr[l]
                    if sum == key:
                        temp = [arr[i], arr[j], arr[k], arr[l]]
                        temp.sort()
                        st.add(tuple(temp))
    ans = [list(x) for x in st]
    return ans

def optimal(arr, target):
    n = len(arr)
    ans = []
    arr.sort()
    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, n):
            if j > i+1 and arr[j] == arr[j-1]:
                continue
            k = j + 1
            l = n - 1
            while k < l:
                sum = arr[i] + arr[j] + arr[k] + arr[l]
                if sum == target:
                    temp = [arr[i], arr[j], arr[k], arr[l]]
                    ans.append(temp)
                    k += 1
                    l -= 1
                    while k < l and arr[k] == arr[k-1]:
                        k += 1
                    while k < l and arr[l] == arr[l+1]:
                        l -= 1
                elif sum < target:
                    k += 1
                else:
                    l -= 1
    return ans


nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
target = 9
ans = brute(nums, target)
print(ans)
ans1 = optimal(nums, target)
print(ans1)
