inputNum = input().split()
a = int(inputNum[0])
b = int(inputNum[1])
c = int(inputNum[2])
if a == b == c:
    money = 10000 + a * 1000
elif a == b or a == c:
    money = 1000 + a * 100
elif b == c:
    money = 1000 + b * 100
else:
    money = max(a, b, c) * 100
print(money)
