n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
sum1 = [0 for i in range(n)]
sum2 = [0 for i in range(n)]

for j in range(len(arr)):
    if j == 0:
        sum1[j] = arr[j]
        sum2[j] = 0
        ans = arr[j]
    elif j == 1:
        sum1[j] = arr[j] + arr[j-1]
        sum2[j] = arr[j]
        ans = arr[0] + arr[1]
    elif j == len(arr) - 1:
        ans = arr[j] + max(sum1[j-2], sum2[j-1])
    else:
        sum1[j] = arr[j] + max(sum1[j-2], sum2[j-1])
        sum2[j] = arr[j] + max(sum1[j-2], sum2[j-2])
print(ans)