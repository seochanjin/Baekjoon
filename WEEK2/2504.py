# import sys
# input = sys.stdin.readline

# a=input()
# len_a = len(a)
# # count1=[0,0]
# # count2=[0,0]

# if a[0] == ')' or a[0] == ']' or a[-1] == '(' or a[-1] =='[':
#     print(0)

# stack=[]

arr=input()
stack=[]

answer=0
tmp=1
for i in range(len(arr)):
    if arr[i] =='(':
        stack.append(arr[i])
        # print(i, 'append 한 후',stack)
        tmp *=2
        # print(i,'tmp :', tmp)
    elif arr[i] == '[':
        stack.append(arr[i])
        # print(i, 'append 한 후',stack)
        tmp *=3
        # print(i, 'tmp :',tmp)
    elif arr[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0 # 실패
            break
        if arr[i-1] == "(":
            answer += tmp
            # print(i,'answer :', answer)
        stack.pop()
        # print(i, 'pop 한 후:',stack)
        tmp //= 2  #tmp 초기화
        # print(i, '초기화 tmp :',tmp)
    else:
        if not stack or stack[-1] == "(":
            answer=0
            break
        if arr[i-1] =='[':
            answer+=tmp
            # print(i,'answer :', answer)
        stack.pop()
        # print(i,'pop 한 후:', stack)
        tmp //=3 #tmp 초기화
        # print(i, '초기화 tmp :',tmp)

if stack:
    print(0)
else:
    print(answer)