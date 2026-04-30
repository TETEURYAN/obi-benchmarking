
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    rects_x1 = [0] * N
    rects_y1 = [0] * N
    rects_x2 = [0] * N
    rects_y2 = [0] * N
    
    idx = 1
    y_coords = set()
    for i in range(N):
        x1 = int(input_data[idx])
        y1 = int(input_data[idx+1])
        x2 = int(input_data[idx+2])
        y2 = int(input_data[idx+3])
        idx += 4
        rects_x1[i] = x1
        rects_y1[i] = y1
        rects_x2[i] = x2
        rects_y2[i] = y2
        y_coords.add(y1)
        y_coords.add(y2)
        
    sorted_y = sorted(list(y_coords))
    comp_Y = {y: i for i, y in enumerate(sorted_y)}
    K = len(sorted_y)
    
    events = []
    for i in range(N):
        events.append((rects_x1[i], 0, i))
        events.append((rects_x2[i], 1, i))
        
    events.sort(key=lambda e: (e[0], e[1]))
    
    INF = K
    tree = [INF] * (2 * K)
    
    parent = [-1] * N
    is_parent = [False] * N
    edge_info = [None] * K
    
    TOP = 0
    BOTTOM = 1
    
    for x, typ, i in events:
        y_top = comp_Y[rects_y1[i]]
        y_bot = comp_Y[rects_y2[i]]
        
        if typ == 0:
            left = y_top + 1 + K
            right = K - 1 + K
            min_y = INF
            while left <= right:
                if left % 2 == 1:
                    if tree[left] < min_y:
                        min_y = tree[left]
                    left += 1
                if right % 2 == 0:
                    if tree[right] < min_y:
                        min_y = tree[right]
                    right -= 1
                left //= 2
                right //= 2
                
            if min_y != INF:
                p_rect, p_edge = edge_info[min_y]
                if p_edge == TOP:
                    parent[i] = p_rect
                else:
                    parent[i] = parent[p_rect]
            else:
                parent[i] = -1
                
            if parent[i] != -1:
                is_parent[parent[i]] = True
                
            edge_info[y_top] = (i, TOP)
            edge_info[y_bot] = (i, BOTTOM)
            
            idx_tree = y_top + K
            tree[idx_tree] = y_top
            idx_tree //= 2
            while idx_tree > 0:
                tree[idx_tree] = tree[2 * idx_tree] if tree[2 * idx_tree] < tree[2 * idx_tree + 1] else tree[2 * idx_tree + 1]
                idx_tree //= 2
                
            idx_tree = y_bot + K
            tree[idx_tree] = y_bot
            idx_tree //= 2
            while idx_tree > 0:
                tree[idx_tree] = tree[2 * idx_tree] if tree[2 * idx_tree] < tree[2 * idx_tree + 1] else tree[2 * idx_tree + 1]
                idx_tree //= 2
                
        else:
            edge_info[y_top] = None
            edge_info[y_bot] = None
            
            idx_tree = y_top + K
            tree[idx_tree] = INF
            idx_tree //= 2
            while idx_tree > 0:
                tree[idx_tree] = tree[2 * idx_tree] if tree[2 * idx_tree] < tree[2 * idx_tree + 1] else tree[2 * idx_tree + 1]
                idx_tree //= 2
                
            idx_tree = y_bot + K
            tree[idx_tree] = INF
            idx_tree //= 2
            while idx_tree > 0:
                tree[idx_tree] = tree[2 * idx_tree] if tree[2 * idx_tree] < tree[2 * idx_tree + 1] else tree[2 * idx_tree + 1]
                idx_tree //= 2
                
    leaves = 0
    for i in range(N):
        if not is_parent[i]:
            leaves += 1
            
    print(leaves)

if __name__ == '__main__':
    solve()
