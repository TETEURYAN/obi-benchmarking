import sys

def main():
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Parse L and C
    L = int(input_data[0])
    C = int(input_data[1])
    
    # Calculate the number of Type 1 tiles
    # Derived from the grid logic: LC + (L-1)(C-1)
    # Simplifies to 2*L*C - L - C + 1
    type1 = 2 * L * C - L - C + 1
    
    # Calculate the number of Type 2 tiles
    # Derived from perimeter coverage: 2*(L-1) + 2*(C-1)
    # Simplifies to 2*L + 2*C - 4
    type2 = 2 * L + 2 * C - 4
    
    # Print the results
    print(type1)
    print(type2)

if __name__ == '__main__':
    main()