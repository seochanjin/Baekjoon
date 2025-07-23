import sys

input = sys.stdin.readline

n = int(input())

a=[]
for i in range(n):
    a.append(int(input()))

mn = a[-1]
cnt = 1
for i in range(n):
    if mn >= a[n-i-1]:
        continue
    else:
        cnt+=1
        mn = a[n-i-1]

print(cnt)