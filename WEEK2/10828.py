import sys

input=sys.stdin.readline

n = int(input())
a=[]
b=[]

for i in range(n):
    a.append(list(input().split()))

    if a[i][0] == 'push':
        b.append(a[i][1])

    elif a[i][0] == 'top':
        if len(b) ==0:
            print(-1)
        else:
            print(b[-1])
    
    elif a[i][0] == 'size':
        print(len(b))

    elif a[i][0] == 'empty':
        if len(b) == 0:
            print(1)
        else:
            print(0)

    elif a[i][0] == 'pop':
        if len(b) == 0:
            print(-1)
        else:
            print(b[-1])
            del b[-1]