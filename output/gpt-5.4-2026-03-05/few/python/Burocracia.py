import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    idx = 0
    n = data[idx]
    idx += 1

    parent = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    parent[1] = 0
    for i in range(2, n + 1):
        p = data[idx]
        idx += 1
        parent[i] = p
        children[p].append(i)

    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    order = [0] * (n + 1)
    depth0 = [0] * (n + 1)

    timer = 0
    stack = [(1, 0)]
    while stack:
        v, state = stack.pop()
        if state == 0:
            timer += 1
            tin[v] = timer
            order[timer] = v
            stack.append((v, 1))
            ch = children[v]
            for u in reversed(ch):
                depth0[u] = depth0[v] + 1
                stack.append((u, 0))
        else:
            tout[v] = timer

    q = data[idx]
    idx += 1

    ops = []
    restruct = []
    for _ in range(q):
        t = data[idx]
        idx += 1
        if t == 1:
            v = data[idx]
            k = data[idx + 1]
            idx += 2
            ops.append((1, v, k))
        else:
            v = data[idx]
            idx += 1
            ops.append((2, v))
            restruct.append(v)

    restruct = sorted(set(restruct), key=lambda x: tin[x])
    m = len(restruct)

    is_special = [False] * (n + 1)
    for v in restruct:
        is_special[v] = True

    special_anc = [0] * (n + 1)
    stack = [1]
    while stack:
        v = stack.pop()
        cur = v if is_special[v] else special_anc[parent[v]]
        special_anc[v] = cur
        for u in children[v]:
            stack.append(u)

    bit = [0] * (m + 2)

    def bit_add(i, delta):
        while i <= m:
            bit[i] += delta
            i += i & -i

    def bit_sum(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    def bit_kth(k):
        pos = 0
        step = 1 << (m.bit_length())
        while step:
            nxt = pos + step
            if nxt <= m and bit[nxt] < k:
                k -= bit[nxt]
                pos = nxt
            step >>= 1
        return pos + 1

    special_tin = [0] * (n + 1)
    for i, v in enumerate(restruct, 1):
        special_tin[v] = i

    active = [False] * (n + 1)

    up = [[0] * (n + 1) for _ in range((n).bit_length())]
    for v in range(1, n + 1):
        up[0][v] = parent[v]
    for j in range(1, len(up)):
        prev = up[j - 1]
        cur = up[j]
        for v in range(1, n + 1):
            cur[v] = prev[prev[v]]

    def kth_ancestor_original(v, k):
        b = 0
        while k:
            if k & 1:
                v = up[b][v]
            k >>= 1
            b += 1
        return v

    out = []

    for op in ops:
        if op[0] == 2:
            v = op[1]
            if not active[v]:
                active[v] = True
                bit_add(special_tin[v], 1)
        else:
            _, v, k = op
            s = special_anc[v]
            if s == 0:
                out.append(str(kth_ancestor_original(v, k)))
                continue

            cnt = bit_sum(special_tin[s])
            if cnt == 0:
                out.append(str(kth_ancestor_original(v, k)))
                continue

            target = depth0[v] - k
            if target >= depth0[s]:
                out.append(str(kth_ancestor_original(v, k)))
            else:
                need = target + 1
                pos = bit_kth(need)
                out.append(str(restruct[pos - 1]))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()