import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print()
        print()
        return
    
    n = int(data[0])
    if n == 0:
        print()
        print()
        return
    
    idx = 1
    max_val = -1
    max_name = ""
    
    for _ in range(n):
        name = data[idx]
        val = int(data[idx + 1])
        idx += 2
        if val > max_val:
            max_val = val
            max_name = name
    
    print(max_name)
    print(max_val)

if __name__ == "__main__":
    main()