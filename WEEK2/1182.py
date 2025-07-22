## 아직 못품

import sys

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

count =0
visited = [0]*n

def sol(add, s):
    global count
    if add == s and sum(visited)>=1:
        count+=1
        return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i]+=1
            add+=nums[i]
            sol(add, s)
            visited[i]=0

sol(0, s)
print(count)


# def sol(idx, total):
#     global count
#     if idx == n:
#         if total == s:
#             count += 1
#         return
    
#     # 현재 숫자를 선택하지 않는 경우
#     sol(idx + 1, total)
#     # 현재 숫자를 선택하는 경우
#     sol(idx + 1, total + nums[idx])

# sol(0, 0)

# # 공집합 제외 조건
# if s == 0:
#     count -= 1

# print(count)






