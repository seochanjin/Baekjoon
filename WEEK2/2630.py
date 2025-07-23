import sys
input = sys.stdin.readline

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
cnt=[0,0]



def sol(x,y,size):

    if  size<1:
        return
    
    total=0
    for i in range(x,size+x):
        for j in range(y,size+y):
            total+=a[i][j]
    if total == size*size:
        cnt[1]+=1
        return
    elif total == 0:
        cnt[0]+=1
        return
    else:
        half = size//2

        sol(x,y,size//2)
        sol(x+half,y,size//2)
        sol(x,half+y, size//2)
        sol(half+x, half+y, size//2)

sol(0, 0, n)
print(cnt[0])
print(cnt[1])


