import heapq
import sys
input = sys.stdin.readline

n = int(input())
a=[]

for i in range(n):
    b = int(input())
    if b == 0:
        if len(a) != 0:
            print(-heapq.heappop(a))
        else:
            print(0)
    else:
        heapq.heappush(a, -b)