from collections import defaultdict, deque
import sys

n, m = map(int, sys.stdin.readline().split())
edge=[]
for _ in range(m):
    edge.append(list(map(int, sys.stdin.readline().split())))

# print(n, m)
# print(edge)

adj = defaultdict(list)

for u, v in edge:
    adj[u].append(v)
    adj[v].append(u)

cnt = 0
bfs_visited=set()

def bfs(start):
    global cnt
    bfs_visited.add(start)
    bfs_deque=deque([start])
    while bfs_deque:
        top = bfs_deque.popleft()
        for b in adj[top]:
            if not b in bfs_visited:
                bfs_deque.append(b)
                bfs_visited.add(b)

for i in range(1, n+1):
    if not i in bfs_visited:
        bfs(i)
        cnt+=1

print(cnt)
