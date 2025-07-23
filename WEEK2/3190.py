import sys
from collections import deque
input=sys.stdin.readline

n = int(input())
k = int(input())

apple=[]
for i in range(k):
    apple.append(list(map(int, input().split())))

l = int(input())

turn = []
for i in range(l):
    turn.append(list(input().split()))

####### 여기까지가 입력값 정리 ##########
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time = 0
direction = 0
turn_idx =0

snake=deque([[1,1]])   

x, y = 1, 1

def check_apple(head):
    if head in apple:
        apple.remove(head)
        return True
    return False

def check_out(head):
    x, y = head
    return not (1 <= x <= n and 1 <= y <= n)

def check_body(head):
    return head in list(snake)[:-1]

def turn_dir(cur, dir):
    if dir == 'D':
        return (cur+1)%4
    else:
        return (cur-1)%4


while True:
    time+=1
    nx = x + dx[direction]
    ny = y + dy[direction]
    head = [nx, ny]

    if check_out(head) or check_body(head):
        break

    snake.append(head)
    if not check_apple(head):
        snake.popleft()

    x, y = nx, ny

    if turn_idx < len(turn) and time == int(turn[turn_idx][0]):
        direction = turn_dir(direction, turn[turn_idx][1])
        turn_idx += 1

print(time)




