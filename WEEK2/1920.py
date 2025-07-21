import sys
input = sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))

a.sort()
c=[0]*m


def solve(start, end, i):
    if start > end:
        return
    mid = (start + end)//2
    if a[mid] == b[i]:
        c[i] = 1
    
    elif a[mid] > b[i]:
        solve(start, mid - 1, i)
    
    else:
        solve(mid + 1, end, i)
    

for i in range(m):
    solve(0, n-1, i)
    print(c[i])