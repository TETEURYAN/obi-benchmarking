import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    test_case_num = 1
    output_buffer = []

    while True:
        try:
            n_str = next(iterator)
            n = int(n_str)
        except StopIteration:
            break
        
        if n == 0:
            break
            
        degree = [0] * 7
        adj = [[] for _ in range(7)]
        
        for _ in range(n):
            x_str = next(iterator)
            y_str = next(iterator)
            x = int(x_str)
            y = int(y_str)
            
            degree[x] += 1
            degree[y] += 1
            adj[x].append(y)
            adj[y].append(x)
            
        # Condição 1: Graus ímpares
        odd_count = 0
        for d in degree:
            if d % 2 != 0:
                odd_count += 1
        
        valid_degree = (odd_count == 0 or odd_count == 2)
        
        # Condição 2: Conectividade
        start_node = -1
        for i in range(7):
            if degree[i] > 0:
                start_node = i
                break
        
        is_connected = True
        if start_node != -1:
            visited = [False] * 7
            stack = [start_node]
            visited[start_node] = True
            count_visited = 0
            
            while stack:
                u = stack.pop()
                if degree[u] > 0:
                    count_visited += 1
                
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            
            total_non_zero = 0
            for d in degree:
                if d > 0:
                    total_non_zero += 1
            
            if count_visited != total_non_zero:
                is_connected = False
        
        output_buffer.append(f"Teste {test_case_num}")
        if valid_degree and is_connected:
            output_buffer.append("sim")
        else:
            output_buffer.append("nao")
        output_buffer.append("")
        
        test_case_num += 1

    print("\n".join(output_buffer))

if __name__ == "__main__":
    solve()