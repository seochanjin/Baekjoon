import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict

n = int(sys.stdin.readline())

edge = [list(map(int, sys.stdin.readline().split())) for _ in range(n-1)]

adj_dict = defaultdict(list)

for a,b in edge:
    adj_dict[a].append(b)
    adj_dict[b].append(a)


visited = set()
check=[0]*(n+1)
before =0

def dfs(start):
    global before
    visited.add(start)
    # print('start :',start)
    check[start]=before
    # print('check : ',check)
    for b in adj_dict[start]:
        if not b in visited:
            before = start
            # print('before : ',before)
            dfs(b)


dfs(1)
for i in range(1, n+1):
    if check[i] != 0:
        print(check[i])

