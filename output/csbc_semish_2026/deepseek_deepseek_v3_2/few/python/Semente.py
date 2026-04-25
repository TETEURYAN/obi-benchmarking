import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    F = int(data[0])
    R = int(data[1])
    drops = list(map(int, data[2:2+R]))
    
    max_gap = 0
    # Gap entre primeira gota e início da fita
    max_gap = max(max_gap, drops[0] - 1)
    # Gap entre última gota e fim da fita
    max_gap = max(max_gap, F - drops[-1])
    
    # Gaps entre gotas consecutivas
    for i in range(1, R):
        gap = drops[i] - drops[i-1] - 1
        # Para gaps ímpares, o tempo é (gap+1)//2
        # Para gaps pares, o tempo é gap//2
        days_needed = (gap + 1) // 2
        max_gap = max(max_gap, days_needed)
    
    print(max_gap)

if __name__ == "__main__":
    main()