from collections import defaultdict
import sys

n = int(sys.stdin.readline())
z=sys.stdin.readline().strip()
a=[0]+list(map(int,z))
# for i in range(n):
#     a.append(int(z[i]))

total=0

adj = defaultdict(list)
edge = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n-1)]
# for i in range(n-1):
#     b=list(map(int, sys.stdin.readline().split()))
#     edge.append(b)

for u, v in edge:
    if a[u] == 1 and a[v] == 1:
        total+=2
    else:
        adj[u].append(v)
        adj[v].append(u)
    

visited = [0]*(n+1)

def dfs(start):
    black = set()
    stack=[start]
    # visited = [False]*(n+1)

    while stack:
        top=stack.pop()
        for e in adj[top]:
            if visited[e] == i:
                continue
            visited[e] = i
            if a[e] ==1:
                black.add(e)
            else:
                stack.append(e)
                    
    count=len(black)
    return count*(count-1)


for i in range(1, n+1):
    if visited[i]== 0 and a[i] == 0:
        visited[i]=i
        total+=dfs(i)
        

print(total)
