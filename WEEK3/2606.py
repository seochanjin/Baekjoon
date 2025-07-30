from collections import deque, defaultdict
import sys

n = int(sys.stdin.readline()) # vertex 수
m = int(sys.stdin.readline()) # edge 수

edge=[] # edge 저장
for _ in range(m):
    edge.append(list(map(int, sys.stdin.readline().split())))

print(edge)

adj = defaultdict(list)

for a, b in edge:
    adj[a].append(b)
    adj[b].append(a)

bfs_visited = set()

def bfs(start):
    
    bfs_visited.add(start)
    bfs_deque = deque([start])

    while bfs_deque:
        top = bfs_deque.popleft()
        for b in adj[top]:
            if not b in bfs_visited:
                bfs_deque.append(b)
                bfs_visited.add(b)


bfs(1)
print(len(bfs_visited)-1)