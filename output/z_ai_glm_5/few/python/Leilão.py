import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    
    max_val = -1
    winner_name = ""
    
    idx = 1
    for _ in range(n):
        if idx + 1 >= len(input_data):
            break
            
        name = input_data[idx]
        val = int(input_data[idx + 1])
        
        if val > max_val:
            max_val = val
            winner_name = name
            
        idx += 2
        
    print(winner_name)
    print(max_val)

if __name__ == "__main__":
    main()