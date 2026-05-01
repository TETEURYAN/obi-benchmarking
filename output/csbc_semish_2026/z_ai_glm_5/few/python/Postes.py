import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    # Pega os N primeiros valores de altura após o inteiro N
    # O slice é 1:n+1 para pegar exatamente N elementos
    heights = map(int, input_data[1:n+1])
    
    substituir = 0
    consertar = 0
    
    for h in heights:
        if h < 50:
            substituir += 1
        elif h < 85:
            consertar += 1
            
    print(substituir, consertar)

if __name__ == "__main__":
    main()