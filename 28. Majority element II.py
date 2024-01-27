def brute(arr):
    n = len(arr)
    ls = []
    for i in range(n):
        if len(ls) == 0 or ls[0] != arr[i]:
            cnt = 0
            for j in range(n):
                if arr[j] == arr[i]:
                    cnt += 1
            if cnt > n//3:
                ls.append(arr[i])
        if len(ls) == 2:
            break
    return ls

def optimal(arr):
    n = len(arr)
    cnt1, cnt2 = 0, 0
    el1, el2 = float('-inf'), float('-inf')
    for i in range(n):
        if cnt1 == 0 and el2 != arr[i]:
            cnt1 += 1
            el1 = arr[i]
        elif cnt2 == 0 and el1 != arr[i]:
            cnt2 += 1
            el2 = arr[i]
        elif arr[i] == el1:
            cnt1 += 1
        elif arr[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    ls = []
    cnt1, cnt2 = 0,0
    for i in range(n):
        if arr[i] == el1:
            cnt1 += 1
        if arr[i] == el2:
            cnt2 += 1
    mini = int(n/3) + 1
    if cnt1 >= mini:
        ls.append(el1)
    if cnt2 >= mini:
        ls.append(el2)
    return ls


arr = [11, 33, 33, 11, 33, 11]
ans = brute(arr)
print(ans)
ans2 = optimal(arr)
print(ans2)
