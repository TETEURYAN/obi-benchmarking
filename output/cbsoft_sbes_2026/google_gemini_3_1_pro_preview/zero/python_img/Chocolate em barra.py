import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    x1 = int(input_data[1])
    y1 = int(input_data[2])
    x2 = int(input_data[3])
    y2 = int(input_data[4])
    
    half = n // 2
    
    if (x1 <= half and x2 > half) or (x1 > half and x2 <= half):
        print("S")
    elif (y1 <= half and y2 > half) or (y1 > half and y2 <= half):
        print("S")
    else:
        print("N")

if __name__ == '__main__':
    main()