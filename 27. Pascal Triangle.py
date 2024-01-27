def var1(n,r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def var2(n):
    ans = 1
    print(ans, end=" ")
    for i in range(1, n):
        ans = ans*(n - i)
        ans = ans // i
        print(ans, end=" ")
    print()

def var3(row):
    ans = 1
    ansrow = [1]
    for col in range(1, row):
        ans *= row-col
        ans = ans // col
        ansrow.append(ans)
    return ansrow

def vari3(n):
    ans = []
    for row in range(1,n+1):
        ans.append(var3(row))
    return ans


r, c = 5, 3
ele = var1(r-1, c-1)
print(ele)
n = 5
var2(n)
m = 5
ans = vari3(m)
print(ans)
for it in ans:
    for ele in it:
        print(ele, end=" ")
    print()
