import sys
from collections import defaultdict,deque

n, m, k, x = map(int, sys.stdin.readline().split())
edge = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# print(edge)
# print(n, m, k, x)

adj = defaultdict(list)
for a, b in edge:
    adj[a].append(b)

cnt = [0]*(n+1)

def bfs(start):
    visited = set()
    bfs_deque = deque([start])
    visited.add(start)

    while bfs_deque:
        top = bfs_deque.popleft()
        
        for d in adj[top]:
            if not d in visited: 
                cnt[d]+=cnt[top]+1
                visited.add(d) # 2,3이 들어감, cnt == 1
                bfs_deque.append(d)



bfs(x)

# print(cnt)

for i in range(len(cnt)):
    if cnt[i] == k:
        print(i)

if not k in cnt:
    print(-1)
