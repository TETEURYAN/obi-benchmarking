import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    left_count = 0
    right_count = 0
    
    if n <= 5:
        left_count = n
        right_count = 0
    else:
        left_count = 5
        right_count = n - 5
        
    left_hand = 'I' * left_count if left_count > 0 else '*'
    right_hand = 'I' * right_count if right_count > 0 else '*'
    
    print(left_hand)
    print(right_hand)

if __name__ == "__main__":
    main()