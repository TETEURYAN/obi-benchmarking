import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        X = int(next(iterator))
        N = int(next(iterator))
    except StopIteration:
        return

    current_quota = X
    
    for _ in range(N):
        try:
            used = int(next(iterator))
        except StopIteration:
            break
        
        current_quota = current_quota - used + X
        
    print(current_quota)

if __name__ == "__main__":
    main()