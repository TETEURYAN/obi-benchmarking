import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    N = int(data[idx])
    idx += 1
    
    pos = [0] * (N + 1)
    
    for i in range(1, N + 1):
        athlete = int(data[idx])
        idx += 1
        pos[athlete] = i
    
    out_lines = []
    for i in range(1, N + 1):
        out_lines.append(str(pos[i]))
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()