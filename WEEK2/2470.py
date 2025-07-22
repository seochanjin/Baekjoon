import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
b=[a[0],a[-1]]

def sol(start, end):
    while start <  end:
        mid = a[start] + a[end]

        if mid == 0:
            print(a[start], a[end])
            break

        elif mid > 0:
            if abs(mid) < abs(b[0]+b[1]):
                b[0]=a[start]
                b[1]=a[end]
            end -= 1
            
        else:
            if abs(mid) < abs(b[0]+b[1]):
                b[0]=a[start]
                b[1]=a[end]
            start += 1

sol(0, n-1)
print(b[0], b[1])
