import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        C = int(next(iterator))
        S = int(next(iterator))
    except StopIteration:
        return

    # O robô inicia na estação 1
    current_station = 1
    count = 0

    # Verifica se a posição inicial é a estação devastada
    if current_station == S:
        count += 1

    # Processa cada comando
    for _ in range(C):
        try:
            cmd = int(next(iterator))
        except StopIteration:
            break
        
        if cmd == 1:
            # Move no sentido horário
            current_station += 1
            if current_station > N:
                current_station = 1
        else:
            # Move no sentido anti-horário
            current_station -= 1
            if current_station < 1:
                current_station = N
        
        # Verifica se permaneceu na estação devastada após o movimento
        if current_station == S:
            count += 1

    print(count)

if __name__ == "__main__":
    main()