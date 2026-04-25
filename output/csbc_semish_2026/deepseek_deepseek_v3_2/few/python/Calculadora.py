
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    N = int(data[0])
    result = 1  # começa com 1
    
    idx = 1
    for _ in range(N):
        digit = int(data[idx])
        op = data[idx + 1]
        idx += 2
        
        if op == '*':
            result *= digit
        else:  # op == '/'
            result //= digit
    
    print(result)

if __name__ == "__main__":
    main()
