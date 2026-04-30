
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    weights = [int(x) for x in input_data[1:n+1]]
    
    if weights[0] > 8:
        print("N")
        return
        
    for i in range(1, n):
        if weights[i] - weights[i-1] > 8:
            print("N")
            return
            
    print("S")

if __name__ == '__main__':
    main()
