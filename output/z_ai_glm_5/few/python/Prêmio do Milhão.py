import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    
    current_sum = 0
    days_count = 0
    target = 1000000
    
    # Iterates through the access counts. 
    # The list contains N integers starting from index 1.
    for i in range(1, n + 1):
        current_sum += int(input_data[i])
        days_count += 1
        
        if current_sum >= target:
            print(days_count)
            return

if __name__ == "__main__":
    main()