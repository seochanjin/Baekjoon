import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
a=[]
for i in range(n):
    a.append(int(input()))

a.sort(reverse=True)
# print(a)
cnt = 0

for c in a:
    if c<=k:
        cnt+=k//c
        k=k%c
        
    
print(cnt)



# def check(i):
#     global cnt, k
#     if i >= len(a):
#         return

#     if a[i] > k:
#         check(i+1)
#     else:
#         k-=a[i]
#         # print('k값 변화:', k)
#         cnt+=1
#         # print('cnt 변화:', cnt)
#         check(i)

# check(0)
# print(cnt)
