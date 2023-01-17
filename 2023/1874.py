n = int(input())
target = []
stack = []
ans = []
for i in range(n):
    target.append(int(input()))

num = 1
flag = False
stack.append(num)
ans.append('+')
for j in range(len(target)):
    if len(stack) == 0:
        num += 1
        ans.append('+')
        stack.append(num)
    if target[j] > stack[-1]:
        while target[j] != stack[-1]:
            num += 1
            if num > n:
                flag = True
                break
            ans.append('+')
            stack.append(num)
        if flag != True:
            ans.append('-')
            stack.pop()
    else:
        ans.append('-')
        stack.pop()
    if num > n: break


if len(stack) == 0:
    for _ in range(len(ans)):
        print(ans[_])
else:
    print("NO")