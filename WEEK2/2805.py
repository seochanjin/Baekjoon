import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a=list(map(int, input().split()))
cut1 = 0
cut2 = max(a)

b=[]

def cut_result(list, cut): # m이 되었으면 좋겠다.
    total = 0
    for i in range(len(list)):
        if list[i] > cut:
            total = total + list[i] -cut
    return total


while cut2 >= cut1:
    mid = ((cut1+cut2))//2
    c = cut_result(a, mid)
    if c >= m:
        b.append([c, mid])
        cut1 = ((cut1+cut2)//2) +1
    
    elif c < m:
        cut2 = ((cut1+cut2)//2) -1

y=b[0][0]
idx=0
for i in range(len(b)):
    if abs(y-m) >= abs(b[i][0]-m):
        y=b[i][0]
        idx=i

print(b[idx][1])
