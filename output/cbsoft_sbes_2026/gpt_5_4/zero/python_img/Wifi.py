import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    rects = []
    events = []
    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        rects.append((x1, y1, x2, y2))
        events.append((x1, 1, -y1, y2, i))  # open
        events.append((x2, 0, -y1, y2, i))  # close

    events.sort()

    parent = [-1] * n
    depth = [0] * n

    import random
    random.seed(0)

    class Node:
        __slots__ = ('key', 'prio', 'left', 'right', 'maxr', 'rid')
        def __init__(self, key, rid):
            self.key = key          # (-y1, y2, id)
            self.prio = random.randint(1, 1 << 30)
            self.left = None
            self.right = None
            self.maxr = key[1]
            self.rid = rid

    def upd(t):
        if t is None:
            return
        t.maxr = t.key[1]
        if t.left is not None and t.left.maxr > t.maxr:
            t.maxr = t.left.maxr
        if t.right is not None and t.right.maxr > t.maxr:
            t.maxr = t.right.maxr

    def split(t, key):
        if t is None:
            return (None, None)
        if t.key < key:
            a, b = split(t.right, key)
            t.right = a
            upd(t)
            return (t, b)
        else:
            a, b = split(t.left, key)
            t.left = b
            upd(t)
            return (a, t)

    def merge(a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a.prio > b.prio:
            a.right = merge(a.right, b)
            upd(a)
            return a
        else:
            b.left = merge(a, b.left)
            upd(b)
            return b

    def insert(t, node):
        if t is None:
            return node
        if node.prio > t.prio:
            a, b = split(t, node.key)
            node.left = a
            node.right = b
            upd(node)
            return node
        if node.key < t.key:
            t.left = insert(t.left, node)
        else:
            t.right = insert(t.right, node)
        upd(t)
        return t

    def erase(t, key):
        if t is None:
            return None
        if key == t.key:
            return merge(t.left, t.right)
        if key < t.key:
            t.left = erase(t.left, key)
        else:
            t.right = erase(t.right, key)
        upd(t)
        return t

    def find_parent(t, negy1, y2):
        cur = t
        ans = None
        while cur is not None:
            if cur.key[0] < negy1:
                cur = cur.right
            else:
                if cur.key[1] < y2:
                    cur = cur.right
                else:
                    ans = cur
                    cur = cur.left
        return ans.rid if ans is not None else -1

    root = None

    for x, typ, negy1, y2, i in events:
        key = (negy1, y2, i)
        if typ == 1:
            p = find_parent(root, negy1, y2)
            parent[i] = p
            depth[i] = 0 if p == -1 else depth[p] + 1
            root = insert(root, Node(key, i))
        else:
            root = erase(root, key)

    leaves_even = 0
    leaves_odd = 0
    has_child = [False] * n
    for i in range(n):
        if parent[i] != -1:
            has_child[parent[i]] = True

    for i in range(n):
        if not has_child[i]:
            if depth[i] % 2 == 0:
                leaves_even += 1
            else:
                leaves_odd += 1

    print(max(leaves_even, leaves_odd))

if __name__ == "__main__":
    main()
