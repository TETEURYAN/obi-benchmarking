import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    N = int(input_data[0])
    P = int(input_data[1])
    
    days = 0
    current = 1
    
    while current * P <= N:
        current *= P
        days += 1
        
    print(days)

if __name__ == "__main__":
    main()