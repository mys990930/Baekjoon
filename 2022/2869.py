import sys

a, b, v = map(int, sys.stdin.readline().split())
height_per_day = a - b

days_taken = (v - a) // height_per_day
if a == v: print('1')
elif (v-a) % height_per_day != 0: print(days_taken + 2)
else: print(days_taken + 1)
