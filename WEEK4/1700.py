import sys
input = sys.stdin.readline

n , k = map(int, input().split())
a = list(map(int, input().split()))

plug =[]
cnt = 0
for i in range(k):
    current = a[i]

    if current in plug:
        continue

    if len(plug) < n:
        plug.append(current)
        continue

    last_used_idx = -1
    target = -1

    for p in plug:
        if p in a[i+1:]:
            idx = a[i+1:].index(p)
        else:
            idx = float('inf')
        if idx > last_used_idx:
            last_used_idx = idx
            target = p
    
    plug.remove(target)
    plug.append(current)
    cnt+=1

print(cnt)





# count=[0]*(max(a)+1)

# for i in range(k):
#     count[a[i]]+=1

# for i in range(k):
#     if len(plug) < n:
#         pops=deque_a.popleft()
#         count[pops]-=1
#         if pops in plug:
#             continue
#         else:
#             plug.append(pops)

# plug.sort()
# print(plug)
# print(count)
# cnt = 0

# while deque_a:
#     node =deque_a.popleft()
#     count[node]-=1
#     maxidx=count.index(max(count))
#     if not node in plug:
#             if maxidx in plug:
#                 # print('최고 인덱스값',maxidx)
#                 for i in range(n):
#                     if plug[i-n+1] == maxidx:
#                         continue
#                     else:
#                         del plug[i-n+1]
#                         plug.append(node)
#                         plug.sort()
#                         cnt+=1
#                         break
#             else:
#                 z=plug.pop()
#                 print('pop값 :',z)
#                 plug.append(node)
#                 plug.sort()
#                 cnt+=1
#     print('cnt갱신값:',cnt)
#     print('heap갱신값',plug)

# print(cnt)
