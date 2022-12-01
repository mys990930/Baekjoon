import sys

arr = [int(sys.stdin.readline().strip()) for i in range(9)]
diff = sum(arr) - 100
suspect = arr.copy()

for i in range(len(suspect)):
    temp = arr.pop(i)
    if diff - temp in arr:
        arr.remove(diff - temp)
        break
    arr.insert(0, temp)

for i in sorted(arr):
    print(i)