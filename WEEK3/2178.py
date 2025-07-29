# from collections import defaultdict, deque
# import sys
# sys.setrecursionlimit(10000)

# n, m = map(int, sys.stdin.readline().split())

# route=[]

# for i in range(n):
#     line= sys.stdin.readline().strip()
#     route.append([int(c) for c in line])

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# visited = [[False]*m for _ in range(n)]
# cnt=0

# def dfs(x,y):
#     global cnt
#     if x>=n or 0>x or y>=m or 0>y:
#         return

#     if visited[x][y] == True or route[x][y]==0:
#         return

#     visited[x][y]=True
#     cnt+=1
#     for i in range(4):
#         dfs(x+dx[i],y+dy[i])
    

# dfs(0,0)
# print(cnt)


##############################################위에 dfs로 풀었음##################

from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())

route=[]

for i in range(n):
    line= sys.stdin.readline().strip()
    route.append([int(c) for c in line])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dist = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def bfs(start, end):
    bfs_deque = deque([(start, end)])
    visited[start][end] = True
    dist[start][end] = 1

    while bfs_deque:
        x, y = bfs_deque.popleft()
        for i in range(4):
            nx, ny = x +dx[i], y + dy[i]
            if 0<=nx<n and 0<= ny <m:
                if not visited[nx][ny] and route[nx][ny] == 1:
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    bfs_deque.append((nx, ny))

bfs(0,0)
print(dist[n-1][m-1])