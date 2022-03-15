def isHansu(num):
    a = str(num)
    if len(a) == 1 or len(a) == 2:
        return True
    elif len(a) == 3:
        if int(a[2]) - int(a[1]) == int(a[1]) - int(a[0]):
            return True
        else:
            return False
    else:
        return False


a = input()
cnt = 1
hansuNumber = 0
while cnt <= int(a):
    if isHansu(cnt):
        hansuNumber += 1
    cnt += 1
print(hansuNumber)
