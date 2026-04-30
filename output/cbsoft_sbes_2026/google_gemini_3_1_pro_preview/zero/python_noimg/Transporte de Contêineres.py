import sys

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) >= 6:
        a = int(input_data[0])
        b = int(input_data[1])
        c = int(input_data[2])
        x = int(input_data[3])
        y = int(input_data[4])
        z = int(input_data[5])
        
        ans = (x // a) * (y // b) * (z // c)
        print(ans)

if __name__ == '__main__':
    main()