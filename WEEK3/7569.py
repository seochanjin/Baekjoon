import sys
input = sys.stdin.readline
from collections import deque, defaultdict

n, m, h = map(int, input().split())

a=[]    

for i in range(h):
    c=[]
    for j in range(m):
        b=list(map(int, input().split()))
        c.append(b)
    a.append(c)

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

start = []

def start_check(): # 시작점 위치 찾기
    for z in range(h):
        for y in range(m):
            for x in range(n):
                if a[z][y][x] == 1:
                    start.append((x, y, z))

def final_check(): # 마지막 체크하기
    max_day = 0
    for z in range(h):
        for y in range(m):
            for x in range(n):
                if a[z][y][x] == 0:
                    print(-1)
                    return
                max_day = max(max_day, a[z][y][x]-1)
    print(max_day)


max_cnt =0

def bfs():
    deque_bfs = deque(start)
    while deque_bfs:
        x, y, z = deque_bfs.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0<=nx<n and 0<= ny <m and 0<=nz<h:
                if a[nz][ny][nx] == 0:
                    a[nz][ny][nx]=a[z][y][x]+1
                    deque_bfs.append((nx,ny,nz))

start_check()

bfs()

final_check()






