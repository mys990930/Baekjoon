a = input().split()
h = int(a[0])
m = int(a[1])
if m >= 45:
    m -= 45
else:
    m = 60 - (45 - m)
    if h == 0:
        h = 23
    else: h -= 1
print(h, m)
