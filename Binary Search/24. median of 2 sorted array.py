def brute(a, b):
    n1, n2 = len(a), len(b)
    arr3 = []
    i, j = 0, 0
    while i < n1 and j < n2:
        if a[i] < b[j]:
            arr3.append(a[i])
            i += 1
        else:
            arr3.append(b[j])
            j += 1
    arr3.extend(a[i:])
    arr3.extend(b[j:])
    n = n1 + n2
    if n % 2 == 1:
        return float(arr3[n // 2])
    median = (arr3[n // 2] + arr3[(n // 2) - 1]) / 2.0
    return median

def better(a, b):
    n1, n2 = len(a), len(b)
    n = n1 + n2
    ind2 = n // 2
    ind1 = ind2 - 1
    cnt = 0
    ind1el, ind2el = -1, -1
    i, j = 0, 0
    while i < n1 and j < n2:
        if a[i] < b[j]:
            if cnt == ind1:
                ind1el = a[i]
            if cnt == ind2:
                ind2el = a[i]
            cnt += 1
            i += 1
        else:
            if cnt == ind1:
                ind1el = b[j]
            if cnt == ind2:
                ind2el = b[j]
            cnt += 1
            j += 1
    while i < n1:
        if cnt == ind1:
            ind1el = a[i]
        if cnt == ind2:
            ind2el = a[i]
        cnt += 1
        i += 1
    while j < n2:
        if cnt == ind1:
            ind1el = b[j]
        if cnt == ind2:
            ind2el = b[j]
        cnt += 1
        j += 1
    if n % 2 == 1:
        return float(ind2el)
    return float(ind1el + ind2el) / 2.0

a = [1, 4, 7, 10, 12]
b = [2, 3, 6, 15]
ans = brute(a,b)
