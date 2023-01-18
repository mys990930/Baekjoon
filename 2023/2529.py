import sys

def solve_max(arr):
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ans = []
    cnt = 1
    for i in range(len(arr) - 1):
        if arr[i] == '<':
            if arr[i + 1] == '>':
                for j in range(cnt):
                    ans.append(max(values) - cnt)
                    values.remove(max(values) - cnt)
                    cnt -= 1
            else:
                cnt += 1
        else:
            if arr[i + 1] == '>':
                ans.append(max(values))
                values.remove(max(values))
                cnt = 0
            else:
                ans.append(max(values))
                values.remove(max(values))
                cnt = 1

    if cnt != 0:
        for k in range(cnt):
            ans.append(max(values) - cnt)
            values.remove(max(values) - cnt)
            cnt -= 1
    else:
        ans.append(max(values))
        values.remove(max(values))
    ans.append(max(values))
    return ans

def solve_min(arr):
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ans = []
    cnt = 1
    for i in range(len(arr) - 1):
        if arr[i] == '>':
            if arr[i + 1] == '<':
                for j in range(cnt):
                    ans.append(min(values) + cnt)
                    values.remove(min(values) + cnt)
                    cnt -= 1
            else:
                cnt += 1
        else:
            if arr[i + 1] == '<':
                ans.append(min(values))
                values.remove(min(values))
                cnt = 0
            else:
                ans.append(min(values))
                values.remove(min(values))
                cnt = 1

    if cnt != 0:
        for k in range(cnt):
            ans.append(min(values) + cnt)
            values.remove(min(values) + cnt)
            cnt -= 1
    else:
        ans.append(min(values))
        values.remove(min(values))
    ans.append(min(values))
    return ans

n = int(input())
array = list(map(str, sys.stdin.readline().split()))
max_ans = solve_max(array)
min_ans = solve_min(array)
print(''.join(str(e) for e in max_ans))
print(''.join(str(e) for e in min_ans))