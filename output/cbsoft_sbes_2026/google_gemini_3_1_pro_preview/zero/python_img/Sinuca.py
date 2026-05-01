import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    row = [int(x) for x in input_data[1:n+1]]
    
    for _ in range(n - 1):
        row = [row[i] * row[i+1] for i in range(len(row) - 1)]
        
    if row[0] == 1:
        print("preta")
    else:
        print("branca")

if __name__ == '__main__':
    main()