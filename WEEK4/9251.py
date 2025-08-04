import sys
input = sys.stdin.readline

a=list(map(str, input().strip()))
b=list(map(str, input().strip()))

# print(a, b)
c=len(a)
d=len(b)

dp =[[0]*(c+1) for _ in range(d+1)]

for i in range(1, d+1):
    for j in range(1, c+1):
        if a[j-1] != b[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = dp[i-1][j-1] + 1

print(dp[d][c])