import sys
from collections import deque, defaultdict
input=sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

adj=defaultdict(list)
indegree = [0]*(n+1)
check = [0]*(n+1)
for i in range(m):
    for j in range(1, a[i][0]):
        adj[a[i][j]].append(a[i][j+1])
        indegree[a[i][j+1]]+=1
        check[a[i][j+1]]+=1
        # print('저장 과정:', indegree)

result=[]

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    result.append(node)
    for e in adj[node]:
        indegree[e]-=1
        if indegree[e] == 0:
            queue.append(e)

if len(result) != n:
    print(0)
else:
    for i in range(len(result)):
        print(result[i])
