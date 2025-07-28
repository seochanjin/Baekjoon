from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

k = int(sys.stdin.readline())
a=[] # [vertex, edge]
b=[]
for i in range(k):
    a.append(list(map(int, sys.stdin.readline().split())))
    c=[list(map(int, sys.stdin.readline().split())) for _ in range(a[i][1])]
    b.append(c)


def dfs(start, c):
    color[start]=c
    for e in adj[start]:
        if color[e] == 0:
            if not dfs(e, -c):
                return False
        elif color[e] ==c:
            return False
    return True


for i in range(k):
    adj=defaultdict(list)
    for w, v in b[i]:
        adj[w].append(v)
        adj[v].append(w)

    color = [0] * (a[i][0]+1)
    check = True

    for j in range(1, a[i][0]+1):
        if color[j] == 0:
            if not dfs(j, 1):
                check = False
                break
    if check == True:
        print("YES")
    else:
        print("NO")

