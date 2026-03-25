
import sys

def main():
    data = sys.stdin.read().split()
    
    if not data:
        return

    D = int(data[0])
    A = int(data[1])
    N = int(data[2])

    num_diarias = 32 - N

    if N < 16:
        valor_diaria = D + (N - 1) * A
    else:
        valor_diaria = D + 14 * A

    total_pagar = num_diarias * valor_diaria

    print(total_pagar)

if __name__ == "__main__":
    main()
