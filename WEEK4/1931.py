import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
queue=deque()
a=[list(map(int, input().split())) for _ in range(n)]
print('정렬 전 리스트 :',a)
a.sort(key=lambda x: (x[1],x[0]))
print('정렬 후 리스트 :',a)
for i in a:
    queue.append(i)
print('큐에 들어간 :',queue)
t=n
cnt =0
while n:
    d=queue.popleft()
    n-=1
    print('빠지는 d: ',d)
    cnt+=1

    for i in range(n):
        if d[1] > queue[0][0]:
            queue.popleft()
            print('전과 비교하고 빠지는 것들:',queue)
            n-=1
        else:
            break
    
    if n==0:
        break

print(cnt)