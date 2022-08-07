import sys

class Card():
    def __init__(self, color, num):
        self.color = color
        self.num = num

def straight_flush():
    if straight() and flush():
        return True
    else:
        return False

def four_cards():
    if cards[1].num == cards[2].num == cards[3].num:
        if cards[0].num == cards[1].num or cards[4].num == cards[1].num:
            return True
        else:
            return False
    else:
        return False

def full_house():
    global high, low
    if cards[0].num == cards[1].num and cards[3].num == cards[4].num:
        if cards[1].num == cards[2].num:
            high = cards[1].num
            low = cards[3].num
            return True
        elif cards[3].num == cards[2].num:
            high = cards[3].num
            low = cards[1].num
            return True
        else:
            return False

def flush():
    for i in range(4):
        if cards[i].color == cards[i + 1].color:
            continue
        else:
            return False
    return True

def straight():
    for i in range(4):
        if cards[i].num - 1 == cards[i + 1].num:
            continue
        else:
            return False
    return True

def triple():
    global high
    for i in range(3):
        if cards[i].num == cards[i + 1].num == cards[i + 2].num:
            high = cards[i].num
            return True
        else:
            continue
    return False

def two_pair():
    global high, low
    for i in range(4):
        if cards[i].num == cards[i + 1].num:
            high = cards[i].num
            break
        else:
            continue
    i += 1
    for i in range(i, 4):
        if cards[i].num == cards[i + 1].num:
            low = cards[i].num
            return True
        else:
            continue
    return False

def one_pair():
    global high
    for i in range(4):
        if cards[i].num == cards[i + 1].num:
            high = cards[i].num
            return True
        else:
            continue
    return False


arr = [sys.stdin.readline().strip() for i in range(5)]
cards = [0]*5
for i in range(5):
    color, num = arr[i].split()
    num = int(num)
    cards[i] = Card(color, num)

cards.sort(key=lambda x: x.num, reverse=True) #편의를 위해 숫자를 내림차순으로 정렬
score = 0
global high, low
high = low = 0

if straight_flush(): score = cards[0].num + 900
elif four_cards(): score = cards[1].num + 800
elif full_house(): score = high * 10 + low + 700
elif flush(): score = cards[0].num + 600
elif straight(): score = cards[0].num + 500
elif triple(): score = high + 400
elif two_pair(): score = high * 10 + low + 300
elif one_pair(): score = high + 200
else: score = cards[0].num + 100

print(score)
