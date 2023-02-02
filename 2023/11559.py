import sys

class Puyo:
    def __init__(self, x, y, color):
        self.x = int(x)
        self.y = int(y)
        self.color = color
    def print(self):
        print("input puyo =", self.x, self.y, self.color)

def dfs(puyo, visited):
    visited.append(puyo)
    near_puyos = find_connected_puyos(puyo)
    for temp_puyo in near_puyos:
        if temp_puyo not in visited:
            dfs(temp_puyo, visited)

def find_connected_puyos(puyo):
    connected_puyos = []
    tempx = [1, 0, 0, -1]
    tempy = [0, 1, -1, 0]
    for _ in range(4):
        x = puyo.x + tempx[_]
        y = puyo.y + tempy[_]
        if -1 < x < 6 and -1 < y < 12:
            if board[y][x].color == puyo.color:
                connected_puyos.append(board[y][x])
    return connected_puyos

def can_relay():
    for i in range(12):
        for j in range(6):
            if board[i][j].color != '.' and board[i][j] not in popable_puyos:
                visited = []
                dfs(board[i][j], visited)
                if len(visited) >= 4:
                    popable_puyos.extend(visited)
    if len(popable_puyos) != 0: return True
    else: return False

def drop_puyos():
    def drop():
        for b in range(i, -1, -1): #빈 위치부터 위로 올라가다가
            if board[b][j].color != '.': #위에 빈칸이 아닌 블럭을 만나면
                for puyo in range(i, -1, -1): #위에 있는 모든 블럭들을 아래칸부터 역순으로
                    if puyo - (i - b) >= 0:
                        board[puyo][j] = Puyo(j, puyo, board[puyo - (i - b)][j].color) # 빈칸의 차만큼 내린다
                        board[puyo - (i - b)][j] = Puyo(j, puyo - (i - b), '.')
                        #board[puyo - (i - b)][j].color = '.' #deep copy되었기 때문에 두 값 모두 .으로 변경되어 버그 발생
                return
    for j in range(6):
        for i in range(11, 0, -1):
            if board[i][j].color == '.': #터져서 빈칸을 만나면
                drop()

def print_board():
    for _ in range(12):
        for __ in range(6):
            print(board[_][__].color, end='')
        print('')
    print('----------------')

arr = [sys.stdin.readline().strip() for _ in range(12)]
board = [[Puyo(0, 0, '.')] * 6 for row in range(12)]
for i in range(12):
    for j in range(6):
        board[i][j]= Puyo(j, i, arr[i][j])

popable_puyos = []

drop_cnt = 0
while can_relay():
    for puyo in popable_puyos:
        puyo.color = '.'
    drop_puyos()
    drop_cnt += 1
    popable_puyos = []

print(drop_cnt)