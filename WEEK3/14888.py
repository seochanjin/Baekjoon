import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
plus, minus, mul, div = map(int, input().split())

result=[]

def dfs(index, re, plus, minus, mul, div):
    if index == n:
        result.append(re)
        return
    
    if plus > 0:
        dfs(index+1, re+nums[index], plus-1, minus, mul, div)
    if minus>0:
        dfs(index+1, re-nums[index], plus, minus-1, mul, div)
    if mul>0:
        dfs(index+1, re*nums[index], plus, minus, mul-1, div)
    if div>0:
        if re < 0:
            dfs(index+1, -(-re//nums[index]),plus, minus, mul, div-1)
        else:
            dfs(index+1, re//nums[index],plus, minus, mul, div-1)

dfs(1, nums[0], plus, minus, mul, div)

print(max(result))
print(min(result))