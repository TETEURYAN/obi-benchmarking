import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    
    # Restrição: 1 ≤ N ≤ 10^5. Se N=0, não há o que processar.
    if n == 0:
        print(0)
        return

    # Converte os elementos da sequência para inteiros.
    # input_data[1] até input_data[n] contêm os números.
    nums = list(map(int, input_data[1:n+1]))
    
    # Dicionário para armazenar a frequência dos elementos na janela atual.
    freq = {}
    left = 0
    max_len = 0
    
    # Algoritmo de Two Pointers (Sliding Window)
    for right in range(n):
        num = nums[right]
        freq[num] = freq.get(num, 0) + 1
        
        # Se encontrarmos um duplicado (frequência > 1), movemos o ponteiro 'left'
        # para a direita até que o intervalo volte a ter apenas números distintos.
        while freq[num] > 1:
            left_num = nums[left]
            freq[left_num] -= 1
            left += 1
            
        # Atualiza o tamanho máximo do intervalo.
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            
    print(max_len)

if __name__ == "__main__":
    solve()