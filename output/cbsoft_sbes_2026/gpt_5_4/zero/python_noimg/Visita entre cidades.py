import sys

def main():
    input = sys.stdin.readline
    N, A, B = map(int, input().split())
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        P, Q, D = map(int, input().split())
        adj[P].append((Q, D))
        adj[Q].append((P, D))
    
    stack = [(A, 0, 0)]  # (cidade, pai, distancia_acumulada)
    while stack:
        u, parent, dist = stack.pop()
        if u == B:
            print(dist)
            return
        for v, w in adj[u]:
            if v != parent:
                stack.append((v, u, dist + w))

if __name__ == "__main__":
    main()
