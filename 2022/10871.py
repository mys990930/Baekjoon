t = input().split()
n = int(t[0])
x = int(t[1])
newList = []
numSeq = input().split()
for i in range(n):
    if int(numSeq[i]) < x:
        newList.append(int(numSeq[i]))
for i in range(len(newList)):
    print(newList[i], end=' ')
