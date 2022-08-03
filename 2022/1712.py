a, b, c = map(int, input().split())
singleProfit = c - b
breakEven = 0
if singleProfit <= 0:
    print("-1")
else:
    breakEven = a // singleProfit + 1
    print(breakEven)