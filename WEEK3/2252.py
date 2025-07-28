#### 위상정렬 gpt 지분 매우 높음 ##### 복습 필수

import sys
from collections import deque, defaultdict

n, m = map(int, sys.stdin.readline().split())

edge = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
adj=defaultdict(list)
indegree = [0]*(n+1)
for a,b in edge:
    adj[a].append(b)
    indegree[b] += 1

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

result=[]

while queue:
    node=queue.popleft()
    result.append(node)

    for b in adj[node]:
        indegree[b] -= 1
        if indegree[b] == 0:
            queue.append(b)

print(*result)


