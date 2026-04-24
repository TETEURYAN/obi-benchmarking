import sys, random

sys.setrecursionlimit(1 << 25)

class Node:
    __slots__ = ('val', 'prio', 'left', 'right', 'size', 'max_val')
    def __init__(self, val):
        self.val = val
        self.prio = random.randrange(1 << 30)
        self.left = None
        self.right = None
        self.size = 1
        self.max_val = val

def update(node):
    node.size = 1
    node.max_val = node.val
    if node.left:
        node.size += node.left.size
        if node.left.max_val > node.max_val:
            node.max_val = node.left.max_val
    if node.right:
        node.size += node.right.size
        if node.right.max_val > node.max_val:
            node.max_val = node.right.max_val

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

def merge(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.prio < b.prio:
        a.right = merge(a.right, b)
        update(a)
        return a
    else:
        b.left = merge(a, b.left)
        update(b)
        return b

def find_last_greater(node, start, X):
    if node is None or node.max_val <= X:
        return -1
    left_size = node.left.size if node.left else 0
    cur_index = start + left_size
    if node.right and node.right.max_val > X:
        return find_last_greater(node.right, cur_index + 1, X)
    if node.val > X:
        return cur_index
    if node.left and node.left.max_val > X:
        return find_last_greater(node.left, start, X)
    return -1

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    alturas = [int(next(it)) for _ in range(N)] if N > 0 else []
    Q = int(next(it))
    root = None
    for h in alturas:
        root = merge(root, Node(h))
    out_lines = []
    for _ in range(Q):
        T = int(next(it))
        I = int(next(it))
        X = int(next(it))
        if T == 0:
            if I == 0:
                left = None
                right = root
            else:
                left, right = split(root, I)
            novo = Node(X)
            root = merge(merge(left, novo), right)
        else:
            if I <= 0:
                out_lines.append("0")
                continue
            left, right = split(root, I - 1)
            mid, right2 = split(right, 1)
            if mid is None:
                resposta = 0
            else:
                altura_I = mid.val
                threshold = altura_I + X
                if left is None:
                    resposta = 0
                else:
                    idx = find_last_greater(left, 1, threshold)
                    resposta = idx if idx != -1 else 0
            root = merge(left, merge(mid, right2))
            out_lines.append(str(resposta))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()