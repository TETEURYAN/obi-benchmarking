import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    N = int(input_data[0])
    G = int(input_data[1])
    M = int(input_data[2])

    total_slices = G * 8 + M * 6
    
    if total_slices > N:
        print(total_slices - N)
    else:
        print(0)

if __name__ == "__main__":
    main()