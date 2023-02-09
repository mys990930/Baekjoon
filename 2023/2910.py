import sys

N, C = map(int, sys.stdin.readline().split())
message = sys.stdin.readline().split()

arr = [[]*i for i in range(1000)]
newdict = {}

for num in message:
    if num in newdict:
        newdict[num] += 1
    else:
        newdict[num] = 1

sorted_dict = sorted(newdict.items(), key = lambda item: item[1], reverse = True)
for i in range(len(sorted_dict)):
    for j in range(int(sorted_dict[i][1])):
        print(sorted_dict[i][0], end = ' ')
