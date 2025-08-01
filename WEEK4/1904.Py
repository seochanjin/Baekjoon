import sys
input = sys.stdin.readline

n = int(input())
a=[0,1,2]

for i in range(1, n-1):
    # print(a[i]+a[i+1])
    a.append(((a[i]+a[i+1]))%15746)
    # print(a)

if n<=2:
    print(a[n])
else:
    b=a[-1]
    print(b)