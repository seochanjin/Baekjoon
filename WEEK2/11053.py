import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
b = []

for i in a:
    idx = bisect_left(b, i)
    if idx == len(b):
        b.append(i)
    else:
        b[idx] = i

print(len(b))

##########################################################################################################################

# import sys
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int, input().split()))

# a.sort()
# b=set(a)

# # print(b)
# print(len(b))

##########################################################################################################################

# import sys
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int, input().split()))
# max_cnt =0

# for i in range(n):
#     cnt = 1
#     for j in range(i-1, n):
#         if a[j-1] < a[j]:
#             cnt+=1
#         else:
#             break
#     max_cnt = max(cnt, max_cnt)

# print(max_cnt)