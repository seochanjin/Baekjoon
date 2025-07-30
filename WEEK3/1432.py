import sys, heapq
from collections import deque, defaultdict

n = int(sys.stdin.readline())
edges = []
for i in range(n):
    edges.append(list(map(int, sys.stdin.readline().strip())))

adj=defaultdict(list)

indegree=[0]*(n+1)

for i in range(n):
    for j in range(n):
        if edges[i][j] == 1:
            adj[i+1].append(j+1)
            indegree[j+1]+=1


visited=[False]*(n+1)
result=[0]*(n+1)
cnt=1

for key in adj:
    adj[key].sort()


heap=[]
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    node = heapq.heappop(heap)
    result[node]=cnt
    cnt+=1
    for b in adj[node]:
        indegree[b]-=1
        if indegree[b] == 0:

            heapq.heappush(heap, b)

if len(result) < n:
    print(-1)
else:
    for i in range(1, n+1):
        print(result[i], end=' ')


#########################
import sys
import bisect
from collections import defaultdict, deque

input = sys.stdin.readline

def propagate_windows(n, out_adj, assigned):
    INF = 10**9
    earliest = [1]*(n+1)
    latest   = [n]*(n+1)
    # 이미 확정된 M_u들은 윈도우를 [m,m]로 고정
    for u, m in assigned.items():
        earliest[u] = latest[u] = m

    # 1) 위상 정렬로 topo 순서 계산
    indeg = [0]*(n+1)
    for u in range(1,n+1):
        for v in out_adj[u]:
            indeg[v] += 1
    dq = deque(u for u in range(1,n+1) if indeg[u]==0)
    topo = []
    while dq:
        u = dq.popleft()
        topo.append(u)
        for v in out_adj[u]:
            indeg[v] -= 1
            if indeg[v]==0:
                dq.append(v)
    if len(topo)<n:
        return None

    # 2) earliest 전파: u→v 이면 earliest[v] ≥ earliest[u]+1
    for u in topo:
        for v in out_adj[u]:
            earliest[v] = max(earliest[v], earliest[u]+1)
    # 3) latest 전파: u→v 이면 latest[u] ≤ latest[v]-1
    for u in reversed(topo):
        for v in out_adj[u]:
            latest[u] = min(latest[u], latest[v]-1)

    # 불가능 윈도우 검출
    for u in range(1,n+1):
        if earliest[u] > latest[u]:
            return None
    return earliest, latest

def can_schedule(n, out_adj, assigned):
    wl = propagate_windows(n, out_adj, assigned)
    if wl is None:
        return False
    earliest, latest = wl

    used = set(assigned.values())
    free_labels = [x for x in range(1,n+1) if x not in used]
    unassigned = [u for u in range(1,n+1) if u not in assigned]

    k = len(free_labels)
    # 각 unassigned u에 대해 [r,d] 계산 (1..k 기준)
    tasks = []
    for u in unassigned:
        r = bisect.bisect_left(free_labels, earliest[u]) + 1
        d = bisect.bisect_right(free_labels, latest[u])
        if r > d:
            return False
        tasks.append((r,d))

    # EDD 그리디 스케줄링: t=1..k
    scheduled = [False]*len(tasks)
    for t in range(1,k+1):
        best = None
        for i,(r,d) in enumerate(tasks):
            if not scheduled[i] and r<=t:
                if best is None or d < tasks[best][1]:
                    best = i
        if best is None or tasks[best][1] < t:
            return False
        scheduled[best] = True

    return True

def main():
    n = int(input())
    mat = [input().rstrip() for _ in range(n)]
    out_adj = defaultdict(list)
    for i in range(n):
        for j,c in enumerate(mat[i]):
            if c=='1':
                out_adj[i+1].append(j+1)

    M = [0]*(n+1)
    assigned = {}

    # 1번 정점부터 N번 정점까지, M[u]를 최소값부터 “시험 → 확정”
    for u in range(1,n+1):
        for x in range(1,n+1):
            if x in assigned.values():
                continue
            assigned[u] = x
            if can_schedule(n, out_adj, assigned):
                M[u] = x
                break
            del assigned[u]

    # 만약 못 매겼으면 -1
    if 0 in M[1:]:
        print(-1)
    else:
        print(*M[1:])

if __name__=="__main__":
    main()