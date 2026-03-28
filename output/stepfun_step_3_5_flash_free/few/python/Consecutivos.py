import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    values = list(map(int, data[1:1+n]))
    
    if n == 0:
        print(0)
        return
        
    max_count = 1
    current_count = 1
    
    for i in range(1, n):
        if values[i] == values[i-1]:
            current_count += 1
        else:
            current_count = 1
        if current_count > max_count:
            max_count = current_count
            
    print(max_count)

if __name__ == "__main__":
    main()