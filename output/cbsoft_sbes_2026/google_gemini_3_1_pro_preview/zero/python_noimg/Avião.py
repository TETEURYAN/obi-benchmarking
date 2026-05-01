import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    F = int(input_data[0])
    C = int(input_data[1])
    E = int(input_data[2])
    B = int(input_data[3])
    
    total_economy_rows = F - E + 1
    total_economy_seats = total_economy_rows * C
    
    if B > total_economy_seats:
        print("PROXIMO VOO")
    else:
        row = E + (B - 1) // C
        seat = chr(ord('A') + (B - 1) % C)
        print(f"{row} {seat}")

if __name__ == '__main__':
    main()