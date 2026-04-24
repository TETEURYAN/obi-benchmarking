import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    idx = 0
    A = int(data[idx]); idx += 1
    L = int(data[idx]); idx += 1
    N = int(data[idx]); idx += 1
    
    photo_min = min(A, L)
    photo_max = max(A, L)
    
    best_id = -1
    best_waste = float('inf')
    
    for frame_id in range(1, N + 1):
        X = int(data[idx]); idx += 1
        Y = int(data[idx]); idx += 1
        
        frame_min = min(X, Y)
        frame_max = max(X, Y)
        
        if photo_min <= frame_min and photo_max <= frame_max:
            waste = (frame_min * frame_max) - (A * L)
            if waste < best_waste or (waste == best_waste and frame_id < best_id):
                best_waste = waste
                best_id = frame_id
    
    print(best_id)

if __name__ == "__main__":
    main()