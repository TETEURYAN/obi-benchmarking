import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    T = int(data[0])
    N = int(data[1])
    cities = sorted(map(int, data[2:2+N]))
    
    min_len = float('inf')
    
    # Segment between first city and border west (0)
    min_len = min(min_len, cities[0])
    
    # Segment between last city and border east (T)
    min_len = min(min_len, T - cities[-1])
    
    # Segments between cities
    for i in range(1, N):
        segment_length = (cities[i] - cities[i-1]) / 2.0
        min_len = min(min_len, segment_length)
    
    print(f"{min_len:.2f}")

if __name__ == "__main__":
    main()