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
        P = 0
        
    possible_count = 0
    
    for _ in range(P):
        try:
            N = int(next(iterator))
            tour = [int(next(iterator)) for _ in range(N)]
        except StopIteration:
            break
            
        is_possible = True
        for i in range(N - 1):
            u = tour[i]
            v = tour[i+1]
            if v not in adj[u]:
                is_possible = False
                break
        
        if is_possible:
            possible_count += 1
            
    print(possible_count)

if __name__ == '__main__':
    solve()