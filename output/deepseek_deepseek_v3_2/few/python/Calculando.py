import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    test_num = 1
    output_lines = []
    
    while idx < len(data):
        m = int(data[idx])
        idx += 1
        if m == 0:
            break
        
        expr = data[idx]
        idx += 1
        
        # Parse expression
        result = 0
        current_num = 0
        sign = 1  # 1 for positive, -1 for negative
        i = 0
        
        while i < len(expr):
            if expr[i].isdigit():
                current_num = current_num * 10 + int(expr[i])
                i += 1
            else:
                result += sign * current_num
                current_num = 0
                sign = 1 if expr[i] == '+' else -1
                i += 1
        
        # Add last number
        result += sign * current_num
        
        output_lines.append(f"Teste {test_num}")
        output_lines.append(str(result))
        output_lines.append("")
        test_num += 1
    
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()