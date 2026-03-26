import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    x = 0
    y = 0
    m2 = m * m
    found = False
    
    for _ in range(n):
        c = data[idx].decode(); idx += 1
        d = int(data[idx]); idx += 1
        
        if c == 'N':
            y += d
        elif c == 'S':
            y -= d
        elif c == 'L':
            x += d
        elif c == 'O':
            x -= d
        
        if x * x + y * y > m2:
            found = True
            break
    
    print(1 if found else 0)

main()