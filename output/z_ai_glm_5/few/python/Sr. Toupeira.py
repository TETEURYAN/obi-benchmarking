import sys

sys.setrecursionlimit(200000)

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
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].add(v)
            adj[v].add(u)
        except StopIteration:
            break
            
    try:
        P = int(next(iterator))
    except StopIteration:
        print(0)
        return

    valid_count = 0
    
    for _ in range(P):
        try:
            N = int(next(iterator))
        except StopIteration:
            break
        
        is_possible = True
        
        try:
            prev = int(next(iterator))
        except StopIteration:
            break
            
        for _ in range(N - 1):
            curr = int(next(iterator))
            
            if is_possible:
                if curr not in adj[prev]:
                    is_possible = False
            
            prev = curr
            
        if is_possible:
            valid_count += 1
            
    print(valid_count)

if __name__ == '__main__':
    solve()