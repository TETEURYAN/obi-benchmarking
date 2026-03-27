import sys

def solve():
    # Fast I/O by reading all input at once
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Use an index to traverse the input tokens
    idx = 0
    try:
        N = int(input_data[idx])
        idx += 1
    except (ValueError, IndexError):
        return

    # Adjacency list to store the graph
    adj = [[] for _ in range(N + 1)]
    
    # Parsing the input
    for i in range(1, N + 1):
        try:
            Mi = int(input_data[idx])
            idx += 1
            
            for _ in range(Mi):
                neighbor = int(input_data[idx])
                idx += 1
                adj[i].append(neighbor)
        except IndexError:
            break
            
    # BFS initialization
    # team array: 0 for Team 1, 1 for Team 2, -1 for unvisited
    team = [-1] * (N + 1)
    team[1] = 0
    
    queue = [1]
    head = 0
    
    # BFS execution
    while head < len(queue):
        u = queue[head]
        head += 1
        
        current_team = team[u]
        next_team = 1 - current_team
        
        for v in adj[u]:
            if team[v] == -1:
                team[v] = next_team
                queue.append(v)
    
    # Collecting results
    team1 = []
    team2 = []
    
    # Iterating 1 to N ensures the output is sorted as required
    for i in range(1, N + 1):
        if team[i] == 0:
            team1.append(i)
        else:
            team2.append(i)
            
    # Output formatting
    print(*team1)
    print(*team2)

if __name__ == '__main__':
    solve()