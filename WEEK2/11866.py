import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


n, k = map(int, input().split())

a=[]
b=[]

for i in range(1, n+1):
    a.append(i)

def sol(idx, k):
    global n
    if n==0:
        return
    idx=(idx+k-1)%n
    # print("a:", a)
    # print("c:",idx)
    # print("n:",n)

    b.append(a[idx])
    # print("b:", b)
    del a[idx]
    n-=1
    sol(idx, k)

sol(0, k)
print('<', end='')
for i in range(len(b)-1):
    print(b[i], end=', ')
print(b[-1], end='')
print('>')
