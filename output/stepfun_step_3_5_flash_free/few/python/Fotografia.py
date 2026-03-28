import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    A = int(data[0])
    L = int(data[1])
    N = int(data[2])
    
    idx = 3
    best_index = -1
    best_excess = None
    
    for i in range(1, N + 1):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        
        if (A <= x and L <= y) or (A <= y and L <= x):
            excess = x * y - A * L
            if best_index == -1 or excess < best_excess or (excess == best_excess and i < best_index):
                best_index = i
                best_excess = excess
    
    print(best_index)

if __name__ == "__main__":
    main()