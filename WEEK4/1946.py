import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스의 개수
n = []
a = []
count=[]
for i in range(t):
    n.append(int(input()))
    c=[list(map(int, input().split())) for _ in range(n[i])]
    c.sort()
    min=c[0][1]
    cnt = 1
    for i in range(1,n[i]):
        if min >= c[i][1]:
            min = c[i][1]
            cnt+=1
    count.append(cnt)

    a.append(c)

for i in range(t):
    print(count[i])

