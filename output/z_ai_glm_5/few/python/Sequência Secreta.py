import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n_str = next(iterator)
        n = int(n_str)
    except StopIteration:
        return

    if n == 0:
        print(0)
        return

    try:
        first_val_str = next(iterator)
        current_val = int(first_val_str)
    except StopIteration:
        print(0)
        return
    
    count = 1
    
    for _ in range(n - 1):
        try:
            next_val_str = next(iterator)
            next_val = int(next_val_str)
            
            if next_val != current_val:
                count += 1
                current_val = next_val
        except StopIteration:
            break
            
    print(count)

if __name__ == '__main__':
    solve()