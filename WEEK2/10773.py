import sys

input = sys.stdin.readline

k = int(input())

a = []

for i in range(k):
    b=int(input())
    if b != 0:
        a.append(b)
    else:
        del a[-1]



print(sum(a))
