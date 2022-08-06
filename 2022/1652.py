import sys

def find_space_number(arr):
    cnt = dot_cnt = space_cnt = 0
    for i in range(len(arr)):
        while cnt < len(arr):
            if arr[i][cnt] == '.':
                dot_cnt += 1
            elif arr[i][cnt] == 'X':
                if dot_cnt >= 2:
                    space_cnt += 1
                dot_cnt = 0
            cnt += 1
        if dot_cnt >= 2:
            space_cnt += 1
        dot_cnt = 0
        cnt = 0
    return space_cnt

def transpose(arr):
    new_array = [[0]*len(arr) for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            new_array[j][i] = arr[i][j]
    return new_array

n = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip() for i in range(n)]
arr2 = transpose(arr)
print(find_space_number(arr), find_space_number(arr2))