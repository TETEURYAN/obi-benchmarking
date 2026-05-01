import sys

def solve():
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token
                
    tokens = get_tokens()
    
    try:
        first = next(tokens)
    except StopIteration:
        return
        
    N = int(first)
    matrix = [next(tokens) for _ in range(N)]
    
    comp = [0] * (N + 1)
    c_id = 1
    
    for i in range(1, N + 1):
        if comp[i] == 0:
            comp[i] = c_id
            row = matrix[i-1]
            for j in range(i + 1, N + 1):
                if row[j-1] == '1':
                    comp[j] = c_id
            c_id += 1
            
    E = int(next(tokens))
    
    out = []
    for _ in range(E):
        K = int(next(tokens))
        seen = set()
        has_friends = False
        for _ in range(K):
            c = int(next(tokens))
            if not has_friends:
                c_comp = comp[c]
                if c_comp in seen:
                    has_friends = True
                else:
                    seen.add(c_comp)
        if has_friends:
            out.append("S")
        else:
            out.append("N")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()