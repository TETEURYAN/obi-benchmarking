import sys

def main():
    # Mapeamento das direções para graus
    # Norte: 0, Leste: 90, Sul: 180, Oeste: 270
    directions = {
        'norte': 0,
        'leste': 90,
        'sul': 180,
        'oeste': 270
    }
    
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    a, b = input_data[0], input_data[1]
    
    angle_a = directions[a]
    angle_b = directions[b]
    
    diff = abs(angle_a - angle_b)
    
    # O menor ângulo é o mínimo entre a diferença direta e o complemento (360 - diff)
    result = min(diff, 360 - diff)
    
    print(result)

if __name__ == '__main__':
    main()