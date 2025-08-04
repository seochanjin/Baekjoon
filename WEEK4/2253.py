import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
dp = [0] * (n+1)

for i in range(m):
    dp[int(input())] = 'M'
max_speed = int((2 * n) ** 0.5) + 2
visited = [[False] * (max_speed+1) for _ in range(n+1)]
queue = deque()
queue.append((1, 0, 0))
visited[1][0] = True

answer = -1

while queue:
    position, speed, count = queue.popleft()
    if position == n:
        answer = count
        break
    for next_speed in [speed-1, speed, speed+1]:
        if next_speed > 0:
            next_position = position + next_speed
            if 1<=next_position <= n and dp[next_position] != 'M' and not visited[next_position][next_speed]:
                visited[next_position][next_speed] = True
                queue.append((next_position, next_speed, count+1))

print(answer)