c = int(input())
for i in range(c):
    a = input().split()
    studentNum = int(a[0])
    a = a[1:]
    tempSum = 0
    for j in range(studentNum):
        tempSum += int(a[j])
    avg = tempSum / studentNum
    superStudent = 0
    for k in range(studentNum):
        if int(a[k]) > avg:
            superStudent += 1
    percentage = superStudent / studentNum * 100
    print(format(percentage, ".3f") + '%')

