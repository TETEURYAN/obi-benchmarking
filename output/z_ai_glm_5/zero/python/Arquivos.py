
import sys

def main():
    # Lê toda a entrada de uma vez para eficiência
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        b = int(next(iterator))
        
        files = []
        for _ in range(n):
            files.append(int(next(iterator)))
    except StopIteration:
        return

    # Ordena os tamanhos dos arquivos
    files.sort()
    
    left = 0
    right = n - 1
    folders = 0
    
    # Algoritmo de dois ponteiros (greedy)
    while left <= right:
        # Tenta emparelhar o menor (left) com o maior (right)
        if files[left] + files[right] <= b:
            left += 1  # O menor arquivo foi usado no par
        
        # O maior arquivo (right) sempre é usado (sozinho ou em par)
        right -= 1
        folders += 1
        
    print(folders)

if __name__ == "__main__":
    main()
