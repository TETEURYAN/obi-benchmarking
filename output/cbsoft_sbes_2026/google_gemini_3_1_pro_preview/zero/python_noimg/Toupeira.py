import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        S = int(next(iterator))
        T = int(next(iterator))
    except StopIteration:
        return
        
    adj = [set() for _ in range(S + 1)]
    
    for _ in range(T):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].add(v)
        adj[v].add(u)
        
    P = int(next(iterator))
    
    possible_walks = 0
    for _ in range(P):
        N = int(next(iterator))
        if N > 0:
            prev = int(next(iterator))
            possible = True
            for _ in range(1, N):
                curr = int(next(iterator))
                if possible and curr not in adj[prev]:
                    possible = False
                prev = curr
            if possible:
                possible_walks += 1
                
    print(possible_walks)

if __name__ == '__main__':
    solve()