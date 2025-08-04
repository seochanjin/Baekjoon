import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

count= [1]*n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            count[i] = max(count[i], count[j]+1)

print(max(count))
