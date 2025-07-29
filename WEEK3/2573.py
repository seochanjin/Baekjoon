import sys
from collections import deque, defaultdict
input=sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]



dx=[0,0,1,-1]
dy=[1,-1,0,0]

def ter():
    tmp = [row[:] for row in a]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                continue
            for k in range(4):
                nx = i +dx[k]
                ny = j +dy[k]
                if 0<=nx<n and 0<=ny<m:
                    if a[nx][ny] == 0:
                        tmp[i][j]-=1
                        if tmp[i][j] <0:
                            tmp[i][j] = 0
    return tmp



def check(x,y, visited):
    queue = deque([(x,y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if 0<=nx<n and 0<=ny<m:
                if a[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    queue.append((nx, ny))

year =0

while True:
    visited = [[False] * m for _ in range(n)]
    cnt=0

    for i in range(n):
        for j in range(m):
            if a[i][j] > 0 and not visited[i][j]:
                check(i, j, visited)
                cnt += 1

    if cnt == 0:
        print(0)
        break
    if cnt >= 2:
        print(year)
        break

    a=ter()
    year+=1




