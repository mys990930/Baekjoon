import sys

class Bomb:
    def __init__(self, c, r):
        self.c = c
        self.r = r
        self.remaining_time = 3

    def explode(self):
        surrounding_bombs = self.get_surrounding_bombs()
        for bomb in surrounding_bombs:
            field[bomb.r][bomb.c] = None
        field[self.r][self.c] = None
        return

    def get_surrounding_bombs(self):
        arr = []
        xlist = [-1, 0, 0, 1]
        ylist = [0, -1, 1, 0]
        for i in range(4):
            tempx = xlist[i]
            tempy = ylist[i]
            if 0 <= self.r + tempx < R and 0 <= self.c + tempy < C:
                temp_bomb = field[self.r + tempx][self.c + tempy]
                if type(temp_bomb) is Bomb:
                    if temp_bomb.remaining_time != 0:
                        arr.append(temp_bomb)
        return arr

def create_init_field(src):
    for i in range(R):
        for j in range(C):
            if src[i][j] == 'O':
                field[i][j] = Bomb(j, i)
            else:
                field[i][j] = None
    return

def plant_bombs():
    for i in range(R):
        for j in range(C):
            if type(field[i][j]) is not Bomb:
                field[i][j] = Bomb(j, i)

def print_field():
    for i in range(R):
        tempstr = str()
        for j in range(C):
            if type(field[i][j]) is Bomb:
                tempstr += 'O'
            else:
                tempstr += '.'
        print(tempstr)

#-------------------------------------------------------
R, C, N = map(int, sys.stdin.readline().split())
arr = []
for i in range(R):
    arr.append(sys.stdin.readline().strip())
#---------------------------------------------------------
field = [[None]*C for _ in range(R)]
create_init_field(arr)

for t in range(0, N): # 0초는 아무것도 하지 않는다
    for i in range(R):
        for j in range(C):
            if type(field[i][j]) is Bomb:
                bomb = field[i][j]
                bomb.remaining_time -= 1
    for i in range(R):
        for j in range(C):
            if type(field[i][j]) is Bomb:
                bomb = field[i][j]
                if bomb.remaining_time == 0:
                    bomb.explode()

    if t % 2 == 1:
        plant_bombs()

print_field()