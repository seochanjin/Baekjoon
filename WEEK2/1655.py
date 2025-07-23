import sys
import heapq

input=sys.stdin.readline

n=int(input())

min_heap=[]
max_heap=[]
heapq.heappush(max_heap, -int(input()))
print(-max_heap[0])

for i in range(n-1):
    heapq.heappush(max_heap, -int(input()))
    if len(max_heap) - len(min_heap) >= 2 or len(min_heap) == 0:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    if -max_heap[0] > min_heap[0]:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    print(-max_heap[0])


