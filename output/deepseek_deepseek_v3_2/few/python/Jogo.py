import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    X = int(data[0])
    output_lines = []
    
    for token in data[1:]:
        T = int(token)
        if T > X:
            output_lines.append("menor")
        elif T < X:
            output_lines.append("maior")
        else:
            output_lines.append("correto")
            break
    
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()