
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    N = int(data[idx])
    K = int(data[idx + 1])
    idx += 2

    parent = [i for i in range(N + 1)]

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    output = []
    for _ in range(K):
        op = data[idx]
        idx += 1
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2

        if op == 'F':
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parent[root_b] = root_a
        elif op == 'C':
            root_a = find(a)
            root_b = find(b)
            output.append('S' if root_a == root_b else 'N')

    print('\n'.join(output))

if __name__ == "__main__":
    main()
