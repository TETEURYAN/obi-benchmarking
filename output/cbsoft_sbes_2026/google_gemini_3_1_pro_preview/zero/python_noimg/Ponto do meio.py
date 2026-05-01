import sys

def solve():
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        resultado = ((1 << n) + 1) ** 2
        print(resultado)

if __name__ == '__main__':
    solve()