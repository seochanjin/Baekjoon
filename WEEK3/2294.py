import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n, k = map(int, input().split())
coins=[int(input()) for _ in range(n)]


visited = [False] * (k+1)

def bfs():
    deque_bfs = deque([(0,0)])
    visited[0] = True
    while deque_bfs:
        current_sum, count = deque_bfs.popleft()
        if current_sum ==k:
            print(count)
            break

        for coin in coins:
            next_sum = current_sum + coin
            if next_sum <= k and not visited[next_sum]:
                visited[next_sum]=True
                deque_bfs.append((next_sum, count+1))

    else:
        print(-1)

bfs()

