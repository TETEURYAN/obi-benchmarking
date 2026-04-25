import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    m_sq = m * m
    
    x, y = 0, 0
    idx = 2
    for _ in range(n):
        direction = data[idx]
        d = int(data[idx + 1])
        idx += 2
        
        if direction == 'N':
            y += d
        elif direction == 'S':
            y -= d
        elif direction == 'L':
            x += d
        elif direction == 'O':
            x -= d
        
        if x * x + y * y > m_sq:
            print(1)
            return
    
    print(0)

if __name__ == "__main__":
    main()