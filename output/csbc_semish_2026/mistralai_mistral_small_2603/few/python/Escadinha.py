
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    seq = list(map(int, data[1:n+1]))
    
    if n <= 2:
        print(n)
        return
        
    count = 1
    current_diff = seq[1] - seq[0]
    current_length = 2
    
    for i in range(2, n):
        diff = seq[i] - seq[i-1]
        if diff == current_diff:
            current_length += 1
        else:
            if current_length >= 2:
                count += 1
            current_diff = diff
            current_length = 2
            
    if current_length >= 2:
        count += 1
        
    print(count)

if __name__ == "__main__":
    main()
