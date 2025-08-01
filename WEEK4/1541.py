import sys
input = sys.stdin.readline

a=input().strip().split('-')
n=len(a)

for i in range(n):
    if '+' in a[i]:
        a[i] = sum(map(int, a[i].split('+')))
o=len(a)

if o == 1:
    print(a[0])
else:
    total = int(a[0])
    for i in range(1,o):
        total-=int(a[i])
    print(total)