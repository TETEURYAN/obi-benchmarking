import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    H = int(data[0])
    M = int(data[1])
    S = int(data[2])
    T = int(data[3])
    
    total_seconds = H * 3600 + M * 60 + S + T
    
    total_seconds %= 24 * 3600
    
    new_H = total_seconds // 3600
    total_seconds %= 3600
    new_M = total_seconds // 60
    new_S = total_seconds % 60
    
    print(new_H)
    print(new_M)
    print(new_S)

if __name__ == "__main__":
    main()