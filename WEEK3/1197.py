import sys
from collections import defaultdict

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return
    if rank[a]<rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a]+=1

v,e = map(int, sys.stdin.readline().split())
edge =[]
for _ in range(e):
    a, b, w = map(int, sys.stdin.readline().split())
    edge.append((w, a, b))

edge.sort()

parent = [i for i in range(v+1)]
rank = [0]*(v+1)
total_w=0

for w, a, b in edge:
    if find(parent, a) != find(parent, b):
        union(parent, rank, a, b)
        total_w += w

print(total_w)