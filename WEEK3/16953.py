import sys
from collections import deque, defaultdict

a, b = map(int, sys.stdin.readline().split())
cnt=0
def div(start):
    global cnt
    while start>a:
        if start%2 == 0:
            start = start//2
            cnt+=1
        elif start%10==1:
            start=start//10
            cnt+=1
        else:
            break

    return start

c=div(b)
if c == a:
    print(cnt+1)
else:
    print(-1)
