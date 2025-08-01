import sys
input = sys.stdin.readline

t = int(input())
a = []
coins = []
money =[]
for i in range(t):
    a.append(int(input()))
    coins.append(list(map(int, input().split())))
    money.append(int(input()))



for i in range(t):
    dp=[0]*(money[i]+1)
    dp[0]=1
    for c in coins[i]:
        for j in range(c,money[i]+1):
            dp[j] += dp[j-c]
    print(dp[money[i]])