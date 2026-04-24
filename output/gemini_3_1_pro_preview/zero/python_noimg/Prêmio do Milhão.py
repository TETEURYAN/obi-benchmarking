
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    total = 0
    days = 0
    
    for i in range(1, n + 1):
        total += int(input_data[i])
        days += 1
        if total >= 1000000:
            break
            
    print(days)

if __name__ == '__main__':
    main()
