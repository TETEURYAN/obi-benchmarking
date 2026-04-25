import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    p = list(map(int, data[1:1+n]))
    
    # Duplicar a lista para simular o círculo
    p_extended = p + p
    
    max_consecutive = 0
    current = 0
    
    for i in range(2*n - 1):
        if p_extended[i] + p_extended[i+1] < 1000:
            current += 1
            max_consecutive = max(max_consecutive, current)
        else:
            current = 0
    
    # Limitar ao máximo possível (n)
    max_consecutive = min(max_consecutive, n)
    print(max_consecutive)

if __name__ == "__main__":
    main()