import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input()) #node의 수
m = int(input()) #edge의 수
edge = [list(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())
adj=defaultdict(list)
rev_adj=defaultdict(list)
indegree = [0]*(n+1)
for a, b, c in edge:
    adj[a].append([b, c])
    rev_adj[b].append([a, c])
    indegree[b]+=1

deque_bfs = deque()
result = [0]*(n+1)
count = 0


for i in range(1,n+1):
    if indegree[i] == 0:
        deque_bfs.append(i)
        # result[i]=0
        # count[i]=0

while deque_bfs:
    node = deque_bfs.popleft()
    for e, w in adj[node]:
        indegree[e]-=1
        r=result[node]+w
        result[e]=max(result[e], r)

        if indegree[e] == 0:
            deque_bfs.append(e)

visited = [False]*(n+1)
q = deque()
q.append(end)
visited[end] = True
count = 0
while q:
    curr = q.popleft()
    for prev, cost in rev_adj[curr]:
        if result[prev]+cost == result[curr]:
            count += 1
            if not visited[prev]:
                visited[prev] = True
                q.append(prev)


print(result[end])
print(count)

