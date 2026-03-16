
import sys

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) < 4:
        return
    
    K = int(input_data[0])
    N = int(input_data[1])
    alphabet = set(input_data[2])
    message = input_data[3]
    
    for char in message:
        if char not in alphabet:
            print("N")
            return
            
    print("S")

if __name__ == '__main__':
    main()
