import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    V = int(data[0])
    P = int(data[1])
    
    base = V // P
    resto = V % P
    
    result = []
    for i in range(P):
        if i < resto:
            result.append(base + 1)
        else:
            result.append(base)
    
    sys.stdout.write("\n".join(map(str, result)))

if __name__ == "__main__":
    main()