import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    pos = [0] * (n + 1)
    
    for i in range(1, n + 1):
        atleta = int(data[i])
        pos[atleta] = i
    
    sys.stdout.write('\n'.join(map(str, pos[1:])))

if __name__ == "__main__":
    main()
