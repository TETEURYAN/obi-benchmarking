import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        M = int(next(iterator))
        N = int(next(iterator))
        
        stock = []
        for _ in range(M):
            row = []
            for _ in range(N):
                row.append(int(next(iterator)))
            stock.append(row)
            
        P = int(next(iterator))
        
        sold_count = 0
        
        for _ in range(P):
            I = int(next(iterator))
            J = int(next(iterator))
            
            # Adjusting to 0-based index
            if stock[I-1][J-1] > 0:
                stock[I-1][J-1] -= 1
                sold_count += 1
                
        print(sold_count)
        
    except StopIteration:
        return

if __name__ == "__main__":
    main()