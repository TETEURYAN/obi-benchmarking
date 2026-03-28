import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    
    # Para cada posição i, contar quantos j > i têm arr[j] < arr[i]
    # Isso pode ser feito com Fenwick Tree (BIT) sobre valores de habilidade
    
    # Primeiro normalizar os valores de habilidade para índice no BIT
    max_val = 100000
    bit = [0] * (max_val + 2)
    
    def bit_update(idx, val):
        while idx <= max_val:
            bit[idx] += val
            idx += idx & -idx
    
    def bit_query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & -idx
        return s
    
    total_pairs = 0
    # Processar da mais nova (última) para a mais antiga (primeira)
    for i in range(n-1, -1, -1):
        val = arr[i]
        # Quantas dançarinas mais novas têm habilidade menor que val?
        count_smaller = bit_query(val - 1)
        total_pairs += count_smaller
        bit_update(val, 1)
    
    print(total_pairs)

if __name__ == "__main__":
    main()