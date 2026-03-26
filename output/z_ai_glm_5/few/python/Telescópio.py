import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    A = int(input_data[0])
    N = int(input_data[1])
    
    threshold = 40000000
    count = 0
    
    # Os fluxos começam no índice 2 do input_data
    # O problema garante que existem N inteiros após os dois primeiros
    for i in range(N):
        F = int(input_data[2 + i])
        if F * A >= threshold:
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()