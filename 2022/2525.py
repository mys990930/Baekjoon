a = input().split()
b = int(input())
h = int(a[0])
m = int(a[1])
m += b
m += h * 60
temph = m // 60
m = m % 60
if temph // 24 >= 1:
    temph -= 24 * (temph // 24)
h = temph
print(h, m)