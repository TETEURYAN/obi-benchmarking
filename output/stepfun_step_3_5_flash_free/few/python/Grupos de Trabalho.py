import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    it = iter(data)
    E = int(next(it))
    M = int(next(it))
    D = int(next(it))
    
    like_pairs = []
    for _ in range(M):
        x = int(next(it))
        y = int(next(it))
        like_pairs.append((x, y))
    
    dislike_pairs = []
    for _ in range(D):
        u = int(next(it))
        v = int(next(it))
        dislike_pairs.append((u, v))
    
    group_of = [0] * (E + 1)
    group_id = 1
    num_groups = E // 3
    for _ in range(num_groups):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        group_of[a] = group_id
        group_of[b] = group_id
        group_of[c] = group_id
        group_id += 1
    
    violations = 0
    for x, y in like_pairs:
        if group_of[x] != group_of[y]:
            violations += 1
    
    for u, v in dislike_pairs:
        if group_of[u] == group_of[v]:
            violations += 1
    
    print(violations)

if __name__ == "__main__":
    main()