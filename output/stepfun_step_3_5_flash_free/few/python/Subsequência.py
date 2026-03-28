import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    A = int(data[0])
    B = int(data[1])
    SA = list(map(int, data[2:2+A]))
    SB = list(map(int, data[2+A:2+A+B]))
    
    j = 0
    for x in SA:
        if j < B and x == SB[j]:
            j += 1
        if j == B:
            break
    
    print('S' if j == B else 'N')

if __name__ == "__main__":
    main()