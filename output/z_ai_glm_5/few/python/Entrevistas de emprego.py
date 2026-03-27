import sys

def solve():
    # Read all input from stdin at once for performance
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
    except StopIteration:
        return

    # DSU (Disjoint Set Union) structures
    parent = list(range(N))
    rank = [0] * N

    # Iterative find with path compression
    def find(i):
        root = i
        while parent[root] != root:
            root = parent[root]
        # Path compression
        while parent[i] != i:
            parent[i], i = root, parent[i]
        return root

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        
        if root_i != root_j:
            # Union by rank
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_j] = root_i
                rank[root_i] += 1

    # Process the friendship matrix
    # Candidates are 0-indexed internally (1 to N in input maps to 0 to N-1)
    for i in range(N):
        try:
            row_str = next(iterator)
        except StopIteration:
            break
        
        # We only need to check j > i because the matrix is symmetric
        # and we don't want to process diagonal or duplicate pairs
        for j in range(i + 1, N):
            if row_str[j] == '1':
                union(i, j)

    # Process interviews
    try:
        E = int(next(iterator))
    except StopIteration:
        E = 0
        
    output = []
    
    for _ in range(E):
        try:
            K_i = int(next(iterator))
        except StopIteration:
            break
            
        roots_in_interview = set()
        conflict_found = False
        
        for _ in range(K_i):
            c_id = int(next(iterator)) - 1 # Convert to 0-based
            
            if conflict_found:
                continue
            
            root = find(c_id)
            if root in roots_in_interview:
                conflict_found = True
            else:
                roots_in_interview.add(root)
        
        if conflict_found:
            output.append("S")
        else:
            output.append("N")

    # Print all results at once
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    solve()