import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    A = int(data[0])
    B = int(data[1])
    SA = list(map(int, data[2:2+A]))
    SB = list(map(int, data[2+A:2+A+B]))
    
    i = 0
    j = 0
    while i < A and j < B:
        if SA[i] == SB[j]:
            j += 1
        i += 1
    
    print('S' if j == B else 'N')

if __name__ == "__main__":
    main()