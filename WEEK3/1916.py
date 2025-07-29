import sys
from collections import defaultdict, deque
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edge = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
start, end = map(int, sys.stdin.readline().split())

# print(edge)
# print(start, end)

adj = defaultdict(list)

for v, u, w in edge:
    adj[v].append((u, w))


result = 0
INF = int(1e9)
cnt=[INF]*(n+1)
cnt[start] = 0
heap = [(0, start)]

while heap:
    cost, node = heapq.heappop(heap)

    if cnt[node] < cost:
        continue
    for a, b in adj[node]:
        if cnt[a] > cost + b:
            cnt[a] = cost + b
            heapq.heappush(heap, (cnt[a], a))

print(cnt[end])