import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
a=[list(map(str, sys.stdin.readline().strip())) for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

d=[]
s=[]
w=[]
def serch_start():
    for i in range(r):
        for j in range(c):
            if a[i][j]=='D':
                d.append([i, j])
            if a[i][j]=='S':
                s.append([i,j])
            if a[i][j] == '*':
                w.append([i,j])

serch_start()

cnt =[[0]*c for _ in range(r)]

visited_s = [[False] * c for _ in range(r)]
visited_w = [[False] * c for _ in range(r)]

def bfs():
    deque_bfs = deque(s)
    deque_water = deque(w)
    while deque_bfs:
        for _ in range(len(deque_water)):
            e, t = deque_water.popleft()
            for i in range(4):
                ne = e + dx[i]
                nt = t + dy[i]
                if 0<=ne<r and 0<= nt <c:
                    if a[ne][nt] == '.' and not visited_w[ne][nt]:
                        visited_w[ne][nt] = True
                        a[ne][nt] = '*'
                        deque_water.append((ne, nt))

        for _ in range(len(deque_bfs)):
            x, y = deque_bfs.popleft()
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if 0<=nx<r and 0<= ny <c:
                    if a[nx][ny] == '.' and not visited_s[nx][ny]:
                        visited_s[nx][ny] = True
                        deque_bfs.append((nx, ny))
                        cnt[nx][ny] = cnt[x][y]+1

                    if a[nx][ny] == 'D':
                        cnt[nx][ny] = cnt[x][y]+1
                        return

bfs()
if cnt[d[0][0]][d[0][1]] == 0:
    print('KAKTUS')
else:
    print(cnt[d[0][0]][d[0][1]])


