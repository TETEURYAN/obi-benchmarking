import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    C = int(data[0])
    A = int(data[1])
    
    # Cada viagem pode levar no máximo C-1 alunos (pois precisa de pelo menos 1 monitor)
    alunos_por_viagem = C - 1
    
    # Número mínimo de viagens = teto(A / alunos_por_viagem)
    viagens = (A + alunos_por_viagem - 1) // alunos_por_viagem
    
    print(viagens)

if __name__ == "__main__":
    main()