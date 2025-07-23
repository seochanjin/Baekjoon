import sys

input = sys.stdin.readline

t=int(input())

for i in range(t):
    cnt = 0
    a = input().strip()      
    if a[0] == ')':
        print('NO')
        continue

    for j in range(len(a)):
        if a[j] == '(':
            cnt+=1
        else:
            cnt-=1
            if cnt <= -1:
                break
    
    if cnt == 0:
        print('YES')
    else:
        print('NO')