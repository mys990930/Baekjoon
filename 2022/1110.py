a = input()
cnt = 0
n = a
if int(n) < 10:
    n = '0' + n[:1]
while True:
    sum = str(int(n[0]) + int(n[1]))
    n = n[-1] + sum[-1]
    cnt += 1
    if int(a) == int(n): break
print(cnt)
