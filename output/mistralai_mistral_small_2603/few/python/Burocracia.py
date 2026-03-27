
import sys
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    p = [0] * (n + 1)
    for i in range(2, n + 1):
        p[i] = int(next(it))

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    for i in range(2, n + 1):
        parent[i] = p[i]
        depth[i] = depth[p[i]] + 1

    q = int(next(it))
    output = []
    for _ in range(q):
        op = int(next(it))
        if op == 1:
            v = int(next(it))
            k = int(next(it))
            current = v
            remaining = k
            while remaining > 0:
                if depth[current] < remaining:
                    break
                if depth[current] - remaining >= 0:
                    current = parent[current]
                    remaining -= 1
                else:
                    break
            output.append(str(current))
        else:
            v = int(next(it))
            stack = [v]
            while stack:
                node = stack.pop()
                if node == 0:
                    continue
                parent[node] = parent[v]
                depth[node] = depth[v] + (depth[node] - depth[parent[v]])
                stack.append(parent[node])
                for i in range(node + 1, n + 1):
                    if parent[i] == node:
                        stack.append(i)

    print('\n'.join(output))

if __name__ == '__main__':
    main()
