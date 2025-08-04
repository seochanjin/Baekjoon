import sys
input = sys.stdin.readline

n, k = map(int, input().split())

a=[1,1]
for i in range(1, n):
    b=[]
    b.append(a[0])
    for j in range(i-1):
        b.append(a[j]+a[j+1])
    b.append(a[-1])
    a=b[:]

print(a[k-1])