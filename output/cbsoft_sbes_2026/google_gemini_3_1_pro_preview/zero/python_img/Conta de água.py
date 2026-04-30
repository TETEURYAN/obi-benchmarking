import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    
    total = 7
    if n > 100:
        total += (n - 100) * 5 + 160
    elif n > 30:
        total += (n - 30) * 2 + 20
    elif n > 10:
        total += (n - 10) * 1
        
    print(total)

if __name__ == '__main__':
    main()