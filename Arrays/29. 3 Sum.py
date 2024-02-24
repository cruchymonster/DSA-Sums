def brute(arr):
    n = len(arr)
    st = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    st.add(tuple(temp))
    ans = [list(item) for item in st]
    return ans

def optimal(arr):
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        if i != 0 and arr[i] == arr[i-1]:
            continue
        j = i +1
        k = n - 1
        while j < k:
            total = arr[i] + arr[j] + arr[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                temp = [arr[i], arr[j], arr[k]]
                ans.append(tuple(temp))
                j += 1
                k -= 1
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1
    return ans
        

arr = [-1, 0, 1, 2, -1, -4]
ans = brute(arr)
print(ans)
ans1 = optimal(arr)
print(ans1)
