from collections import defaultdict, deque
import sys

adj = defaultdict(list)
n, m, v = map(int, sys.stdin.readline().split())
edge=[]
for _ in range(m):
        edge.append((map(int, sys.stdin.readline().split())))

for a, b in edge:
    adj[a].append(b)
    adj[b].append(a)

for key in adj:
    adj[key].sort()

visited = set()

def dfs(start):
    visited.add(start)
    print(start,end=' ')
    for b in adj[start]:
        if not b in visited:
            dfs(b)



def bfs(start):
    visited_bfs = set()
    bfs_deque = deque([start])
    visited_bfs.add(start)

    while bfs_deque:
        top = bfs_deque.popleft()
        print(top, end=' ')
        for b in adj[top]:
            if not b in visited_bfs:
                visited_bfs.add(b)
                bfs_deque.append(b)


dfs(v)
print()
bfs(v)