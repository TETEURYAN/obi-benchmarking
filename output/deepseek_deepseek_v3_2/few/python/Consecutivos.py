
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    n = int(data[0])
    values = list(map(int, data[1:1+n]))
    
    max_len = 1
    curr_len = 1
    
    for i in range(1, n):
        if values[i] == values[i-1]:
            curr_len += 1
        else:
            curr_len = 1
        max_len = max(max_len, curr_len)
    
    print(max_len)

if __name__ == "__main__":
    main()
