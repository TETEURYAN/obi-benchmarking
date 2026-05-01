
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    
    rooms = []
    idx = 1
    y_coords = set()
    
    for i in range(1, N + 1):
        x1 = int(data[idx])
        y1 = int(data[idx+1])
        x2 = int(data[idx+2])
        y2 = int(data[idx+3])
        idx += 4
        
        rooms.append((x1, y1, x2, y2, i))
        y_coords.add(y1)
        y_coords.add(y2)
        
    sorted_y = sorted(list(y_coords))
    M = len(sorted_y)
    
    y_to_idx = {y: i + 1 for i, y in enumerate(sorted_y)}
    idx_to_y = [0] * (M + 1)
    for i, y in enumerate(sorted_y):
        idx_to_y[i + 1] = y
        
    events = []
    for x1, y1, x2, y2, i in rooms:
        events.append((x1, 1, y1, y2, i))
        events.append((x2, 0, y1, y2, i))
        
    events.sort()
    
    tree = [0] * (M + 1)
    log_size = M.bit_length()
    
    active_edges = {}
    
    P = [0] * (N + 1)
    is_leaf = [True] * (N + 1)
    
    TOP = 1
    BOTTOM = 0
    total_active_edges = 0
    
    for event in events:
        x = event[0]
        etype = event[1]
        y1 = event[2]
        y2 = event[3]
        room_id = event[4]
        
        if etype == 1:
            idx_y1 = y_to_idx[y1]
            
            s = 0
            curr = idx_y1
            while curr > 0:
                s += tree[curr]
                curr -= curr & (-curr)
            k = s + 1
            
            if k > total_active_edges:
                P[room_id] = 0
            else:
                curr_idx = 0
                curr_k = k
                for i in range(log_size, -1, -1):
                    next_idx = curr_idx + (1 << i)
                    if next_idx <= M and tree[next_idx] < curr_k:
                        curr_idx = next_idx
                        curr_k -= tree[next_idx]
                next_idx = curr_idx + 1
                
                if next_idx <= M:
                    next_y = idx_to_y[next_idx]
                    edge_type, edge_room = active_edges[next_y]
                    if edge_type == TOP:
                        P[room_id] = edge_room
                    else:
                        P[room_id] = P[edge_room]
                    is_leaf[P[room_id]] = False
                else:
                    P[room_id] = 0
            
            active_edges[y1] = (TOP, room_id)
            active_edges[y2] = (BOTTOM, room_id)
            
            curr = idx_y1
            while curr <= M:
                tree[curr] += 1
                curr += curr & (-curr)
                
            curr = y_to_idx[y2]
            while curr <= M:
                tree[curr] += 1
                curr += curr & (-curr)
                
            total_active_edges += 2
            
        else:
            curr = y_to_idx[y1]
            while curr <= M:
                tree[curr] -= 1
                curr += curr & (-curr)
                
            curr = y_to_idx[y2]
            while curr <= M:
                tree[curr] -= 1
                curr += curr & (-curr)
                
            del active_edges[y1]
            del active_edges[y2]
            total_active_edges -= 2
            
    ans = sum(1 for i in range(1, N + 1) if is_leaf[i])
    print(ans)

if __name__ == '__main__':
    solve()
