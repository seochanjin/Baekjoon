import sys
import heapq
input = sys.stdin.readline
n = int(input())
case = []

for _ in range(n):
    home, ofc = map(int, input().split())
    start = min(home, ofc)
    end = max(home, ofc)
    case.append((start, end))

case.sort(key=lambda x: x[1])
rail_len = int(input())
heap = []
max_count = 0

for start, end in case:
    heapq.heappush(heap, start)
    while heap and heap[0] < end - rail_len:
        heapq.heappop(heap)
    max_count = max(max_count, len(heap))
    
print(max_count)