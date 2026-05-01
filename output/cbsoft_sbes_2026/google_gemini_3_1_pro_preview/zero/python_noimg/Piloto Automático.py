import sys

def main():
    lines = sys.stdin.read().split()
    if len(lines) >= 3:
        A = int(lines[0])
        B = int(lines[1])
        C = int(lines[2])
        
        if B - A < C - B:
            print(1)
        elif B - A > C - B:
            print(-1)
        else:
            print(0)

if __name__ == '__main__':
    main()