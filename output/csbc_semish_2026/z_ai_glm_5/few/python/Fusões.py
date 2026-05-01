import sys

sys.setrecursionlimit(200000)

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        k = int(next(iterator))
    except StopIteration:
        return

    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        
        if root_i != root_j:
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_j] = root_i
                rank[root_i] += 1

    output = []
    
    for _ in range(k):
        try:
            op = next(iterator)
            a = int(next(iterator))
            b = int(next(iterator))
            
            if op == 'F':
                union(a, b)
            elif op == 'C':
                if find(a) == find(b):
                    output.append('S')
                else:
                    output.append('N')
        except StopIteration:
            break
            
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    main()