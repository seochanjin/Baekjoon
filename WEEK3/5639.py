import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
write = sys.stdout.write

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node, data):
    while True:
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                break
            else:
                node = node.left
        else:
            if node.right is None:
                node.right = Node(data)
                break
            else:
                node = node.right

def postorder(node, result):
    if node is None:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(str(node.data))

data = sys.stdin.read().split()
preorder = list(map(int, data))

root = Node(preorder[0])
for value in preorder[1:]:
    insert(root, value)

result =[]
postorder(root, result)
write('\n'.join(result))




