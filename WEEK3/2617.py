import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

adjmax=defaultdict(list)
adjmin=defaultdict(list)

for v, w in a:
    adjmax[v].append(w)
    adjmin[w].append(v)

mid = n//2

def bfs(start, adj):
    visited = [False]*(n+1)
    q=deque([start])
    visited[start]=True
    cnt=0
    while q:
        node=q.popleft()
        for e in adj[node]:
            if not visited[e]:
                visited[e]=True
                cnt+=1
                q.append(e)
    return cnt

answer = 0
for i in range(1, n+1):
    heavy = bfs(i, adjmax)
    light = bfs(i, adjmin)
    if heavy > mid or light > mid:
        answer+=1

print(answer)