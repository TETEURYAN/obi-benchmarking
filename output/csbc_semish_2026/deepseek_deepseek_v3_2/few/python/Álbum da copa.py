import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    
    album = set()
    for _ in range(M):
        x = int(data[idx]); idx += 1
        if 1 <= x <= N:
            album.add(x)
    
    faltam = N - len(album)
    print(faltam)

if __name__ == "__main__":
    main()