import sys
input=sys.stdin.readline
from collections import defaultdict, deque
INF = float('inf')
#### 입력
n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

dp = [[INF] * n for _ in range(1 << n)]
dp[1][0] =0

for mask in range(1<<n):
    for i in range(n):
        if dp[mask][i] == INF:
            continue
        for j in range(n):
            if mask & (1<<j):
                continue
            if w[i][j] == 0:
                continue
            next_mask = mask | (1 << j)
            dp[next_mask][j] = min(dp[next_mask][j], dp[mask][i]+w[i][j])

ans = INF
final_mask = (1<<n) - 1
for i in range(n):
    if w[i][0] == 0:
        continue
    ans = min(ans, dp[final_mask][i] + w[i[0]])

print(ans)
