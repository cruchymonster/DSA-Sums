def Max(Arr):
    maxProfit = 0
    mini = Arr[0]

    for i in range(1, len(Arr)):
        curProfit = Arr[i] - mini
        maxProfit = max(maxProfit, curProfit)
        mini = min(mini, Arr[i])

    return maxProfit

Arr = [7, 1, 5, 3, 6, 4]
print("The maximum profit by selling the stock is", Max(Arr))
