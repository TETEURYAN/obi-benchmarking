import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    K = int(data[0])
    N = int(data[1])
    alfabeto = data[2]
    mensagem = data[3]
    
    allowed = set(alfabeto)
    for char in mensagem:
        if char not in allowed:
            print('N')
            return
    print('S')

if __name__ == "__main__":
    main()