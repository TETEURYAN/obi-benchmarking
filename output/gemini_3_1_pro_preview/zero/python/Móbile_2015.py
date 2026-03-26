import sys

def main():
    lines = sys.stdin.read().split()
    if len(lines) >= 4:
        A = int(lines[0])
        B = int(lines[1])
        C = int(lines[2])
        D = int(lines[3])
        
        if A == B + C + D and B + C == D and B == C:
            print("S")
        else:
            print("N")

if __name__ == '__main__':
    main()