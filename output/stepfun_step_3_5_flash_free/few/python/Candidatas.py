import sys
import math

sys.setrecursionlimit(300000)

class Node:
    __slots__ = ('full', 'pref', 'suff', 'ans', 'length', 'left', 'right')
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.full = 0
        self.pref = {}
        self.suff = {}
        self.ans = 0
        self.length = 0

def pull(node):
    left = node.left
    right = node.right
    node.length = left.length + right.length
    node.full = math.gcd(left.full, right.full)

    node.pref = {}
    for md, cnt in left.pref.items():
        node.pref[md] = node.pref.get(md, 0) + cnt
    for md, cnt in right.pref.items():
        md_new = math.gcd(left.full, md)
        node.pref[md_new] = node.pref.get(md_new, 0) + cnt

    node.suff = {}
    for md, cnt in right.suff.items():
        node.suff[md] = node.suff.get(md, 0) + cnt
    for md, cnt in left.suff.items():
        md_new = math.gcd(md, right.full)
        node.suff[md_new] = node.suff.get(md_new, 0) + cnt

    total_A = left.length
    total_B = right.length
    A1 = left.suff.get(1, 0)
    B1 = right.pref.get(1, 0)
    cross = A1 * total_B + (total_A - A1) * B1
    for mdA, cntA in left.suff.items():
        if mdA == 1:
            continue
        for mdB, cntB in right.pref.items():
            if mdB == 1:
                continue
            if math.gcd(mdA, mdB) == 1:
                cross += cntA * cntB
    node.ans = left.ans + right.ans + cross

def build(arr, l, r):
    node = Node()
    if l == r:
        val = arr[l]
        node.full = val
        node.pref = {val: 1}
        node.suff = {val: 1}
        node.ans = 1 if val == 1 else 0
        node.length = 1
        node.left = None
        node.right = None
    else:
        mid = (l + r) // 2
        node.left = build(arr, l, mid)
        node.right = build(arr, mid+1, r)
        pull(node)
    return node

def update(node, l, r, idx, val):
    if l == r:
        node.full = val
        node.pref = {val: 1}
        node.suff = {val: 1}
        node.ans = 1 if val == 1 else 0
        node.length = 1
        return
    mid = (l + r) // 2
    if idx <= mid:
        update(node.left, l, mid, idx, val)
    else:
        update(node.right, mid+1, r, idx, val)
    pull(node)

def query(node, l, r, ql, qr):
    if ql <= l and r <= qr:
        return node
    mid = (l + r) // 2
    left_node = None
    right_node = None
    if ql <= mid:
        left_node = query(node.left, l, mid, ql, qr)
    if qr > mid:
        right_node = query(node.right, mid+1, r, ql, qr)
    if left_node is None:
        return right_node
    if right_node is None:
        return left_node
    temp = Node()
    temp.left = left_node
    temp.right = right_node
    pull(temp)
    return temp

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    S = [int(next(it)) for _ in range(N)]
    root = build(S, 0, N-1)
    out_lines = []
    for _ in range(M):
        t = int(next(it))
        if t == 1:
            I = int(next(it)) - 1
            V = int(next(it))
            update(root, 0, N-1, I, V)
        else:
            E = int(next(it)) - 1
            D = int(next(it)) - 1
            node = query(root, 0, N-1, E, D)
            total_subarrays = (D - E + 1) * (D - E + 2) // 2
            ans = total_subarrays - node.ans
            out_lines.append(str(ans))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()