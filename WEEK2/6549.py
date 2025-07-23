import sys
input = sys.stdin.readline

a=[]
while True:
    b=list(map(int, input().split()))
    if b[0] == 0:
        break
    a.append(b)

num = []
h = []
for i in range(len(a)):
    num.append(a[i][0])
    h.append(a[i][1:len(a[i])])


max_sum = [0] * len(num)

for i in range(len(num)):
    stack=[]
    for j in range(num[i]):
        while stack and h[i][stack[-1]] > h[i][j]:
                top=stack.pop()
                height = h[i][top]
                width = j if not stack else j-stack[-1]-1
                max_sum[i]=max(height*width, max_sum[i])
        stack.append(j)

    j = num[i]
    while stack:
        top=stack.pop()
        height = h[i][top]
        width = j if not stack else j-stack[-1]-1
        max_sum[i]=max(height*width, max_sum[i]) 

for i in range(len(num)):
    print(max_sum[i])







####### 이건 N^{2} ############
# import sys
# input = sys.stdin.readline

# a=[]
# while True:
#     b=list(map(int, input().split()))
#     if b[0] == 0:
#         break
#     a.append(b)

# num = []
# h = []
# for i in range(len(a)):
#     num.append(a[i][0])
#     h.append(a[i][1:len(a[i])])


# def sol(h):
#     n = len(h)
#     max_area=0

#     uni_h = sorted(set(h))

#     for i in uni_h:
#         width =0
#         max_width =0
#         for j in range(n):
#             if h[j] >= i:
#                 width +=1
#                 max_width = max(max_width, width)
#             else:
#                 width =0
#         area = i*max_width
#         max_area=max(max_area, area)

#     return max_area

# for k in range(len(num)):
#     print(sol(h[k]))


