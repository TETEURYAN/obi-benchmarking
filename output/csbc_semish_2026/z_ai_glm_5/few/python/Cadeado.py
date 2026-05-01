import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n_str = next(iterator)
        n = int(n_str)
    except StopIteration:
        return

    total_clicks = 0
    
    for _ in range(n):
        try:
            c_str = next(iterator)
            s_str = next(iterator)
            c = int(c_str)
            s = int(s_str)
            
            diff = abs(c - s)
            total_clicks += min(diff, 10 - diff)
        except StopIteration:
            break
            
    print(total_clicks)

if __name__ == "__main__":
    main()