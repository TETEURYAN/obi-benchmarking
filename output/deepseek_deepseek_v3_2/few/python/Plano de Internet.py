import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    idx = 0
    X = int(data[idx]); idx += 1
    N = int(data[idx]); idx += 1
    
    quota_atual = 0
    for _ in range(N):
        usado = int(data[idx]); idx += 1
        quota_atual += X - usado
    
    print(quota_atual + X)

if __name__ == "__main__":
    main()