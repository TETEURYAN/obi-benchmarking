import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    it = 0
    n = data[it]
    it += 1

    parent0 = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    parent0[1] = 0
    for i in range(2, n + 1):
        p = data[it]
        it += 1
        parent0[i] = p
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

    q = data[it]
    it += 1

    ops = []
    restruct = []
    for _ in range(q):
        t = data[it]
        it += 1
        if t == 1:
            v = data[it]
            k = data[it + 1]
            it += 2
            ops.append((1, v, k))
        else:
            v = data[it]
            it += 1
            ops.append((2, v))
            restruct.append(v)

    m = len(restruct)
    if m == 0:
        LOG = n.bit_length()
        up = [[0] * (n + 1) for _ in range(LOG)]
        up[0] = parent0[:]
        for j in range(1, LOG):
            uj = up[j]
            prev = up[j - 1]
            for v in range(1, n + 1):
                uj[v] = prev[prev[v]]

        out = []
        for op in ops:
            if op[0] == 1:
                v, k = op[1], op[2]
                b = 0
                while k:
                    if k & 1:
                        v = up[b][v]
                    k >>= 1
                    b += 1
                out.append(str(v))
        sys.stdout.write("\n".join(out))
        return

    restruct.sort(key=lambda x: tin[x])

    parent_virtual = [0] * (m + 1)
    node_of = [0] * (m + 1)
    idx_of_node = {}
    for i, v in enumerate(restruct, 1):
        node_of[i] = v
        idx_of_node[v] = i

    stack_nodes = []
    for i, v in enumerate(restruct, 1):
        while stack_nodes and tout[node_of[stack_nodes[-1]]] < tin[v]:
            stack_nodes.pop()
        parent_virtual[i] = stack_nodes[-1] if stack_nodes else 0
        stack_nodes.append(i)

    LOGM = (m + 1).bit_length()
    upv = [[0] * (m + 1) for _ in range(LOGM)]
    upv[0] = parent_virtual[:]
    for j in range(1, LOGM):
        prev = upv[j - 1]
        cur = upv[j]
        for i in range(1, m + 1):
            cur[i] = prev[prev[i]]

    starts = [tin[v] for v in restruct]
    ends = [tout[v] for v in restruct]

    def deepest_restruct_ancestor(v):
        x = tin[v]
        lo, hi = 0, m - 1
        pos = -1
        while lo <= hi:
            mid = (lo + hi) >> 1
            if starts[mid] <= x:
                pos = mid
                lo = mid + 1
            else:
                hi = mid - 1
        if pos == -1:
            return 0
        if x <= ends[pos]:
            return pos + 1
        return 0

    out = []
    for op in ops:
        if op[0] == 2:
            continue

        v, k = op[1], op[2]
        a = deepest_restruct_ancestor(v)

        if a == 0:
            if k <= depth0[v]:
                cur = v
                kk = k
                while kk:
                    cur = parent0[cur]
                    kk -= 1
                out.append(str(cur))
            else:
                rem = k - depth0[v]
                cur_idx = 0
                cur = 1
                out.append(str(cur))
        else:
            va = node_of[a]
            dist_to_a = 1 if v != va else 0
            if k <= dist_to_a:
                if k == 0:
                    out.append(str(v))
                else:
                    out.append(str(va))
                continue

            rem = k - dist_to_a
            cur_idx = a

            b = 0
            while b < LOGM:
                anc = upv[b][cur_idx]
                if anc != 0:
                    d = depth0[node_of[cur_idx]] - depth0[node_of[anc]]
                    if d < rem:
                        rem -= d
                        cur_idx = anc
                b += 1

            if rem == 0:
                out.append(str(node_of[cur_idx]))
            else:
                target_depth = depth0[node_of[cur_idx]] - rem
                cur = node_of[cur_idx]
                while depth0[cur] > target_depth:
                    cur = parent0[cur]
                out.append(str(cur))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()