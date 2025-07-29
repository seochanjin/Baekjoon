from collections import defaultdict, deque
import sys
input=sys.stdin.readline

n = int(input())
m = int(input())
edge=[list(map(int, input().split())) for _ in range(m)]

adj = defaultdict(list)
outdegree = [0] * (n+1)
indegree = [0] * (n+1)
for x, y, k in edge:
    adj[x].append([y, k])
    indegree[y]+=1
    outdegree[x]+=1

result = [0]*(n+1)

list=[]

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        result[i] = 1
        queue.append(i)
    if outdegree[i] == 0:
        list.append(i)

while queue:
    node=queue.popleft()
    # result.append(node)

    for b, w in adj[node]:
        result[b]= result[b]+ (w*result[node])
        indegree[b]-=1
        if indegree[b] == 0:
            queue.append(b)

for i in list:
    print(i, result[i])

