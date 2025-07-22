import sys
input = sys.stdin.readline

n, c = map(int, input().split())
a=[]

for i in range(n):
    a.append(int(input()))
a.sort()

def sol(dstnc):
    cnt = 1
    last = a[0]

    for i in range(1, n):
        if a[i] - last >=dstnc:
            cnt +=1
            last = a[i]
    return cnt >= c




def b_serch(start, end):
    result = 0
    while start<=end:
        mid = (start+end)//2

        if sol(mid):
            result = mid
            start = mid + 1
        else:
            end = mid -1

    return result





print(b_serch(1, a[-1]- a[0]))



