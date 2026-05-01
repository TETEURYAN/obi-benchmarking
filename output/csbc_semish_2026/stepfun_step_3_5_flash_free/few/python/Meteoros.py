import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    test_num = 1
    out_lines = []
    
    while idx < len(data):
        x1 = int(data[idx]); y1 = int(data[idx+1]); x2 = int(data[idx+2]); y2 = int(data[idx+3])
        idx += 4
        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            break
        
        n = int(data[idx]); idx += 1
        count = 0
        for _ in range(n):
            x = int(data[idx]); y = int(data[idx+1]); idx += 2
            if x1 <= x <= x2 and y2 <= y <= y1:
                count += 1
        
        out_lines.append(f"Teste {test_num}")
        out_lines.append(str(count))
        out_lines.append("")
        test_num += 1
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()