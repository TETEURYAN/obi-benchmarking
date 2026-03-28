import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    digits = list(map(int, input_data[1:1+n]))
    
    last_digit = digits[-1]
    
    # The problem states the input number is not divisible by 5, 
    # so last_digit is not 0 or 5.
    
    best_sequence = None
    
    # Iterate through all positions except the last one to find valid swaps
    for i in range(n - 1):
        # A swap results in a number divisible by 5 if the digit at position i
        # is 0 or 5 (since it will move to the last position).
        if digits[i] == 0 or digits[i] == 5:
            # Create a copy of the digits list
            current_sequence = digits[:]
            # Perform the swap
            current_sequence[i], current_sequence[-1] = current_sequence[-1], current_sequence[i]
            
            # Update best_sequence if this is the first valid swap or if it's larger
            # than the previous best. Python list comparison is lexicographical.
            if best_sequence is None or current_sequence > best_sequence:
                best_sequence = current_sequence
                
    if best_sequence is None:
        print("-1")
    else:
        print(*(best_sequence))

if __name__ == '__main__':
    solve()