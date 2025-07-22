# ###### 스택 없이 반복문으로 ######

# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# a = list(input().rstrip())

# cnt=n - k

# i=0
# while cnt > 0 and i < len(a) -1:
#     if a[i] < a[i+1]:
#         del a[i]
#         cnt-=1
#     else:
#         i+=1  

# while cnt>0:
#     a.pop()
#     cnt-=1

# print(''.join(a))


###### 스택으로 ######

import sys
input = sys.stdin.readline

n, k=map(int, input().split())
a= input().rstrip()

result = []
to_delete = k

for digit in a:
    while result and to_delete > 0 and result[-1] < digit:
        result.pop()
        to_delete -= 1
    result.append(digit)

print(''.join(result[:n-k]))