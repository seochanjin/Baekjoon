import sys

input = sys.stdin.readline

n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
    

def sol(add, b):
    global count
    if add == a[b]:
        count+=1
        return
    
    for j in range(1, 4):
        if add+j > a[b]:
            continue
        else:
            sol(add+j, b)




for i in range(n):
    count =0
    sol(0,i)
    print(count)