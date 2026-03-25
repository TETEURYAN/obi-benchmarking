import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    seq = list(map(int, data[1:1+n]))
    
    if n == 1:
        print(1)
        return
    
    escadas = 0
    i = 0
    while i < n:
        j = i + 1
        if j < n:
            diff = seq[j] - seq[i]
        while j < n and seq[j] - seq[j-1] == diff:
            j += 1
        escadas += 1
        i = j - 1
    
    print(escadas)

if __name__ == "__main__":
    main()