import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        A = int(next(iterator))
        L = int(next(iterator))
        N = int(next(iterator))
    except StopIteration:
        return

    min_photo = min(A, L)
    max_photo = max(A, L)
    
    best_index = -1
    min_area = float('inf')
    
    for i in range(1, N + 1):
        try:
            X = int(next(iterator))
            Y = int(next(iterator))
        except StopIteration:
            break
            
        min_frame = min(X, Y)
        max_frame = max(X, Y)
        
        if min_photo <= min_frame and max_photo <= max_frame:
            current_area = X * Y
            if current_area < min_area:
                min_area = current_area
                best_index = i
                
    print(best_index)

if __name__ == "__main__":
    solve()