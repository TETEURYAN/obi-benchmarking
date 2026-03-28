
import sys
import random

class Node:
    __slots__ = ('altura', 'priority', 'left', 'right', 'size', 'max_height')
    def __init__(self, altura):
        self.altura = altura
        self.priority = random.random()
        self.left = None
        self.right = None
        self.size = 1
        self.max_height = altura

def update(node):
    if node is None:
        return
    node.size = 1
    if node.left:
        node.size += node.left.size
    if node.right:
        node.size += node.right.size
    node.max_height = node.altura
    if node.left and node.left.max_height > node.max_height:
        node.max_height = node.left.max_height
    if node.right and node.right.max_height > node.max_height:
        node.max_height = node.right.max_height

def split(node, k):
    if node is None:
        return (None, None)
    left_size = node.left.size if node.left else 0
    if k <= left_size:
        left, right = split(node.left, k)
        node.left = right
        update(node)
        return (left, node)
    else:
        left, right = split(node.right, k - left_size - 1)
        node.right = left
        update(node)
        return (node, right)

def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    if left.priority > right.priority:
        left.right = merge(left.right, right)
        update(left)
        return left
    else:
        right.left = merge(left, right.left)
        update(right)
        return right

def get_min(node):
    if node is None:
        return None
    while node.left:
        node = node.left
    return node

def find_last_greater(node, limiar, offset):
    if node is None:
        return None
    if node.right and node.right.max_height > limiar:
        new_offset = offset + (node.left.size if node.left else 0) + 1
        return find_last_greater(node.right, limiar, new_offset)
    elif node.altura > limiar:
        pos = offset + (node.left.size if node.left else 0) + 1
        return pos
    elif node.left and node.left.max_height > limiar:
        return find_last_greater(node.left, limiar, offset)
    else:
        return None

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    alturas = [int(next(it)) for _ in range(N)] if N > 0 else []
    Q = int(next(it))
    t = None
    for h in alturas:
        node = Node(h)
        t = merge(t, node)
    out_lines = []
    for _ in range(Q):
        T = int(next(it))
        I = int(next(it))
        X = int(next(it))
        if T == 0:
            new_node = Node(X)
            if I == 0:
                t = merge(new_node, t)
            else:
                left, right = split(t, I)
                t = merge(merge(left, new_node), right)
        else:
            left, right = split(t, I-1)
            node_I = get_min(right)
            if node_I is None:
                pos = None
            else:
                h = node_I.altura
                limiar = h + X
                pos = find_last_greater(left, limiar, 0)
            t = merge(left, right)
            out_lines.append("0" if pos is None else str(pos))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
