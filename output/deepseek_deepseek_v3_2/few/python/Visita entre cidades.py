import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    A = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        P = int(next(it))
        Q = int(next(it))
        D = int(next(it))
        adj[P].append((Q, D))
        adj[Q].append((P, D))
    
    stack = [(A, 0, -1)]
    while stack:
        node, dist, parent = stack.pop()
        if node == B:
            print(dist)
            return
        for neighbor, w in adj[node]:
            if neighbor != parent:
                stack.append((neighbor, dist + w, node))

if __name__ == "__main__":
    main()