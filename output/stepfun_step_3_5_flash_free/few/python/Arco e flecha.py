import sys

MAX_VAL = 2500000000000

class Node:
    __slots__ = ('left', 'right', 'sum')
    def __init__(self):
        self.left = None
        self.right = None
        self.sum = 0

def update(node, l, r, pos):
    if node is None:
        node = Node()
    node.sum += 1
    if l == r:
        return node
    mid = (l + r) // 2
    if pos <= mid:
        node.left = update(node.left, l, mid, pos)
    else:
        node.right = update(node.right, mid+1, r, pos)
    return node

def query(node, l, r, ql, qr):
    if node is None:
        return 0
    if ql > r or qr < l:
        return 0
    if ql <= l and r <= qr:
        return node.sum
    mid = (l + r) // 2
    return query(node.left, l, mid, ql, qr) + query(node.right, mid+1, r, ql, qr)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    xs = []
    ys = []
    idx = 1
    for i in range(n):
        x = int(data[idx]); y = int(data[idx+1]); idx += 2
        xs.append(x)
        ys.append(y)
    
    root = None
    prev_penalty = 0
    out_lines = []
    for i in range(n):
        if i == 0:
            xr = xs[i]
            yr = ys[i]
        else:
            xr = xs[i] + prev_penalty
            yr = ys[i] + prev_penalty
        d2 = xr*xr + yr*yr
        p = query(root, 0, MAX_VAL, 0, d2) if root is not None else 0
        out_lines.append(str(p))
        root = update(root, 0, MAX_VAL, d2)
        prev_penalty = p
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()