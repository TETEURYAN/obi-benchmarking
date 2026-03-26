import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    grades = map(int, input_data[1:n+1])
    
    # As notas estão entre 0 e 100, podemos usar um array de contagem.
    # Isso é mais eficiente que um dicionário para intervalos pequenos e discretos.
    counts = [0] * 101
    
    for g in grades:
        counts[g] += 1
        
    max_freq = -1
    best_grade = -1
    
    # Iteramos de 0 a 100.
    # Como queremos a maior nota em caso de empate, usamos >=.
    # Se counts[i] == max_freq, o i maior (atual) substituirá o anterior.
    for i in range(101):
        if counts[i] >= max_freq:
            max_freq = counts[i]
            best_grade = i
            
    print(best_grade)

if __name__ == "__main__":
    main()