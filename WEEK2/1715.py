import heapq
import sys
input = sys.stdin.readline

n = int(input())
a=[]
for i in range(n):
    heapq.heappush(a, int(input()))

# print('초기저장값: ', a)
total=0

while len(a) != 1:
    b=heapq.heappop(a)
    c=heapq.heappop(a)
    total = total+b+c
    heapq.heappush(a, b+c)

print(total)