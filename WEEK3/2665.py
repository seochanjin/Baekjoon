import sys
from collections import deque, defaultdict
input=sys.stdin.readline

n = int(input())
a = [list(map(int, input().strip())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[float('inf')]*n for _ in range(n)]
visited[0][0] = 0
# print(visited)


def bfs(start, end):
    deque_bfs=deque([(start, end)])
    # visited[start][end] == True
    while deque_bfs:
        x,y = deque_bfs.popleft()
        for i in range(4):
            nx, ny = x +dx[i], y + dy[i]
            if 0<=nx<n and 0<= ny <n:
                if a[nx][ny] == 1:
                    cost = 0
                else:
                    cost = 1
                
                if visited[nx][ny] > visited[x][y] + cost:
                    visited[nx][ny] = visited[x][y] + cost

                    if cost == 0:
                        deque_bfs.appendleft((nx, ny))
                    else:
                        deque_bfs.append((nx, ny))

bfs(0,0)

print(visited[n-1][n-1])
                



