import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    A = int(data[0])
    N = int(data[1])
    M = int(data[2])
    
    rows = []
    idx = 3
    for _ in range(N):
        row = list(map(int, data[idx:idx+M]))
        rows.append(row)
        idx += M
    
    for i in range(N-1, -1, -1):
        consecutive = 0
        for seat in rows[i]:
            if seat == 0:
                consecutive += 1
                if consecutive >= A:
                    print(N - i)
                    return
            else:
                consecutive = 0
    print(-1)

if __name__ == "__main__":
    main()