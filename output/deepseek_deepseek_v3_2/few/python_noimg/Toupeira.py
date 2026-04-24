import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    S = int(next(it))
    T = int(next(it))
    
    adj = [set() for _ in range(S + 1)]
    for _ in range(T):
        x = int(next(it))
        y = int(next(it))
        adj[x].add(y)
        adj[y].add(x)
    
    P = int(next(it))
    possible_count = 0
    
    for _ in range(P):
        N = int(next(it))
        path = [int(next(it)) for _ in range(N)]
        valid = True
        for i in range(N - 1):
            if path[i + 1] not in adj[path[i]]:
                valid = False
                break
        if valid:
            possible_count += 1
    
    print(possible_count)

if __name__ == "__main__":
    main()