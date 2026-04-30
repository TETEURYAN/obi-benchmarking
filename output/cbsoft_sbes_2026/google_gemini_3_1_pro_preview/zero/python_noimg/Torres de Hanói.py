import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    test_number = 1
    for item in input_data:
        n = int(item)
        if n == 0:
            break
        
        moves = (1 << n) - 1
        print(f"Teste {test_number}")
        print(moves)
        print()
        
        test_number += 1

if __name__ == '__main__':
    main()