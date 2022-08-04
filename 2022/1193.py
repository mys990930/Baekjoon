a = int(input())
n = sum = 1
while sum + n <= a:
    sum += n
    n += 1
d = a - sum
print(1+d, "/", n-d, sep='') if n % 2 == 0 else print(n-d, "/", 1+d, sep='')