import math

a = int(input())
N = (-3 + math.sqrt(12 * (a - 1) + 9)) / 6
result = math.ceil(N) + 1
print(result)
