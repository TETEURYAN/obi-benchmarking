import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    # Ler a sequência de alturas
    a = list(map(int, input_data[1:n+1]))
    
    # Verificar a condição de vale (pico múltiplo)
    # A[i-1] > A[i] < A[i+1]
    for i in range(1, n - 1):
        if a[i-1] > a[i] and a[i] < a[i+1]:
            print("S")
            return
            
    print("N")

if __name__ == "__main__":
    solve()