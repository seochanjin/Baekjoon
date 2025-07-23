# import sys

# input = sys.stdin.readline

# n = int(input())

# a = list(map(int, input().split()))

# b = [0]*n

# for i in range(n):
#     for j in range(n-1-i):
#         if a[n-i-1]<=a[n-1-i-j-1]:
#             b[i]=n-1-i-j
#             break

# for i in range(n):
#     print(b[n-i-1], end=' ')





import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))
stack = []  # (index, height)
result = [0] * n

for i in range(n):
    current_height = heights[i]

    # 스택에서 현재 탑보다 낮은 탑들은 제거
    while stack and stack[-1][1] < current_height:
        stack.pop()

    if stack:
        result[i] = stack[-1][0]  # 수신할 수 있는 탑의 인덱스 (1-based)
    else:
        result[i] = 0  # 수신할 수 있는 탑이 없음

    stack.append((i + 1, current_height))  # 현재 탑을 스택에 저장 (1-based index)

print(' '.join(map(str, result)))


