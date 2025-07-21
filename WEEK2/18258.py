import sys
from collections import deque

input=sys.stdin.readline

n = int(input())
a=[]
b=[]
b = deque()
c=0

for i in range(n):
    a.append(list(input().split()))

    if a[i][0] == 'push':
        b.append(a[i][1])
        c+=1

    elif a[i][0] == 'front':
        if c ==0:
            print(-1)
        else:
            print(b[0])
    
    elif a[i][0] == 'size':
        print(c)

    elif a[i][0] == 'empty':
        if c == 0:
            print(1)
        else:
            print(0)

    elif a[i][0] == 'pop':
        if c == 0:
            print(-1)
        else:
            print(b.popleft())
            c-=1
    
    elif a[i][0] == 'back':
        if c == 0:
            print(-1)
        else:
            print(b[-1])