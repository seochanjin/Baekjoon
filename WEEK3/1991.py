import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

n = int(input())
tree ={}

for _ in range(n):
    root, left, right = input().strip().split()

    if root not in tree:
        tree[root] = Node(root)

    if left != '.':
        tree[left] = Node(left)
        tree[root].left = tree[left]

    if right != '.':
        tree[right] = Node(right)
        tree[root].right = tree[right]

def preorder(node):
    if node is None:
        return
    print(node.data, end='')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end='')
    inorder(node.right)
    

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end='')


preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])