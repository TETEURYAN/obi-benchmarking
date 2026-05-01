import sys

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        C = int(input_data[0])
        A = int(input_data[1])
        
        viagens = (A + C - 2) // (C - 1)
        print(viagens)

if __name__ == '__main__':
    main()