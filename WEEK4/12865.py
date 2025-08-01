import sys
input = sys.stdin.readline

n, k = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]

# a.sort()

def check():
    for i in range(1, n+1):
        w = a[i-1][0]
        v = a[i-1][1]
        for j in range(k+1):
            # print('인덱스 확인:',i, j)
            if w > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j-w]+v, dp[i-1][j])
            # print('dp확인:', dp)

check()
print(dp[n][k])