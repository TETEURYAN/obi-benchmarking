import sys

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    N = int(data[0])
    P = int(data[1])
    
    dias = 0
    quantidade = 1
    while quantidade * P <= N:
        quantidade *= P
        dias += 1
    print(dias)

if __name__ == "__main__":
    main()