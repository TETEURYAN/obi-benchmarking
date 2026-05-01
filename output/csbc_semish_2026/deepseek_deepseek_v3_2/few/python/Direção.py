import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    A, B = data[0], data[1]
    
    dir_map = {'norte': 0, 'leste': 90, 'sul': 180, 'oeste': 270}
    ang_a = dir_map[A]
    ang_b = dir_map[B]
    
    diff = abs(ang_a - ang_b)
    ans = min(diff, 360 - diff)
    print(ans)

if __name__ == "__main__":
    main()