import sys

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) >= 6:
        A = int(input_data[0])
        B = int(input_data[1])
        C = int(input_data[2])
        X = int(input_data[3])
        Y = int(input_data[4])
        Z = int(input_data[5])
        
        ans = (X // A) * (Y // B) * (Z // C)
        print(ans)

if __name__ == '__main__':
    main()