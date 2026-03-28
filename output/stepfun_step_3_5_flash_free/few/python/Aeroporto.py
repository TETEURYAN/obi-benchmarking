import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    test_num = 1
    out_lines = []
    
    while idx < len(data):
        A = int(data[idx]); V = int(data[idx+1]); idx += 2
        if A == 0 and V == 0:
            break
        
        count = [0] * (A + 1)
        for _ in range(V):
            x = int(data[idx]); y = int(data[idx+1]); idx += 2
            count[x] += 1
            count[y] += 1
        
        max_traffic = max(count[1:]) if A >= 1 else 0
        airports = [str(i) for i in range(1, A+1) if count[i] == max_traffic]
        
        out_lines.append(f"Teste {test_num}")
        out_lines.append(" ".join(airports))
        out_lines.append("")
        test_num += 1
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()