import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    parents = list(map(int, input_data[2:N+2]))
    present = set(map(int, input_data[N+2:]))
    
    adj = [[] for _ in range(N + 1)]
    for i, p in enumerate(parents):
        adj[p].append(i + 1)
        
    gen_total = []
    gen_present = []
    
    queue = [(0, 0)]
    while queue:
        next_queue = []
        total_count = 0
        present_count = 0
        
        for node, depth in queue:
            for child in adj[node]:
                total_count += 1
                if child in present:
                    present_count += 1
                next_queue.append((child, depth + 1))
        
        if not next_queue:
            break
            
        gen_total.append(total_count)
        gen_present.append(present_count)
        queue = next_queue
        
    results = []
    for i in range(len(gen_total)):
        percentage = (gen_present[i] / gen_total[i]) * 100
        results.append(f"{percentage:.2f}")
        
    print(" ".join(results))

if __name__ == '__main__':
    solve()