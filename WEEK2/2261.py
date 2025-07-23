import sys
input = sys.stdin.readline
n = int(input())
points = []

for _ in range(n):
    a, b = map(int, input().split())
    points.append((a, b))

points.sort()

def distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def divide(start, end):
    if end - start <= 3:
        min_dist = float('inf')   #min구할거니까 무한대로 초기화
        for i in range(start, end):
            for j in range(i + 1, end):
                dist = distance(points[i], points[j])
                min_dist = min(min_dist, dist)
        return min_dist
    mid = (start + end) // 2
    d_left = divide(start, mid)
    d_right = divide(mid, end)
    d = min(d_left,d_right)
    mid_x = points[mid][0]
    candidates = []
    for i in range(start, end):
        if (points[i][0] - mid_x)**2 <= d:
            candidates.append(points[i])
    candidates.sort(key=lambda x: x[1])
    for i in range(len(candidates)):
        for j in range(i+1, len(candidates)):
            if (candidates[j][1] - candidates[i][1])**2 >= d:
                break
            if j - i > 7:
                break
            d = min(d, distance(candidates[i], candidates[j]))
    return d

print(divide(0, n))