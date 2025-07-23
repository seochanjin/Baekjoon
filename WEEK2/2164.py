import sys
from collections import deque

input = sys.stdin.readline

n=int(input())
a=[]
a=deque()

for i in range(1, n+1):
    a.append(i)

b=len(a)
c=0

while True:
    if b == 1:
        break
    else:
        a.popleft()
        b-=1

    if b==1:
        break
    else:
        a.append(a.popleft())

print(a[0])