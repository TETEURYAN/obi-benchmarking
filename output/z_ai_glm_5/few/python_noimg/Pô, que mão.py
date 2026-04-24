import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    costs = [int(input_data[1]), int(input_data[2]), int(input_data[3])]
    
    costs.sort()
    
    count = 0
    remaining = n
    
    for cost in costs:
        if remaining >= cost:
            remaining -= cost
            count += 1
        else:
            break
            
    print(count)

if __name__ == "__main__":
    main()