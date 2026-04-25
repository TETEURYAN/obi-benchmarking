import sys
import random

sys.setrecursionlimit(200000)

class Node:
    def __init__(self, h):
        self.h = h
        self.prior = random.randint(0, 1 << 60)
        self.size = 1
        self.max_h = h
        self.left = None
        self.right = None

def size(node):
    return node.size if node else 0

def update(node):
    if not node:
        return
    node.size = 1 + size(node.left) + size(node.right)
    node.max_h = node.h
    if node.left:
        node.max_h = max(node.max_h, node.left.max_h)
    if node.right:
        node.max_h = max(node.max_h, node.right.max_h)

def split(node, k):
    if not node:
        return None, None
    if size(node.left) >= k:
        left, node.left = split(node.left, k)
        update(node)
        return left, node
    else:
        node.right, right = split(node.right, k - size(node.left) - 1)
        update(node)
        return node, right

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left.prior > right.prior:
        left.right = merge(left.right, right)
        update(left)
        return left
    else:
        right.left = merge(left, right.left)
        update(right)
        return right

def get_kth(node, k):
    if not node:
        return None
    if size(node.left) >= k:
        return get_kth(node.left, k)
    if size(node.left) + 1 == k:
        return node
    return get_kth(node.right, k - size(node.left) - 1)

def find_rightmost(node, val, base):
    if not node or node.max_h <= val:
        return 0
    if node.right and node.right.max_h > val:
        return find_rightmost(node.right, val, base + size(node.left) + 1)
    if node.h > val:
        return base + size(node.left) + 1
    return find_rightmost(node.left, val, base)

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
heights = []
for i in range(N):
    heights.append(int(input_data[idx]))
    idx += 1
Q = int(input_data[idx])
idx += 1
root = None
for h in heights:
    new_node = Node(h)
    root = merge(root, new_node)
for _ in range(Q):
    T = int(input_data[idx])
    I = int(input_data[idx + 1])
    X = int(input_data[idx + 2])
    idx += 3
    if T == 0:
        pos = I + 1 if I > 0 else 1
        left, right = split(root, pos - 1)
        new_node = Node(X)
        root = merge(merge(left, new_node), right)
    else:
        node = get_kth(root, I)
        val = node.h + X
        left, right = split(root, I - 1)
        pos = find_rightmost(left, val, 0)
        root = merge(left, right)
        print(pos)