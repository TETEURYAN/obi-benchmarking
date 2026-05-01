import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    idx = 2
    
    x = 0
    y = 0
    max_dist_squared = m * m
    
    for i in range(n):
        dir_char = data[idx]
        dist = int(data[idx + 1])
        idx += 2
        
        if dir_char == 'N':
            y += dist
        elif dir_char == 'S':
            y -= dist
        elif dir_char == 'L':
            x += dist
        elif dir_char == 'O':
            x -= dist
        
        current_dist_squared = x * x + y * y
        if current_dist_squared > max_dist_squared:
            print(1)
            return
    
    print(0)

if __name__ == "__main__":
    main()