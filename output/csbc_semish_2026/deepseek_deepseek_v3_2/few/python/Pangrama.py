import sys

def main():
    alfabeto = set('abcdefghijlmnopqrstuvxz')
    linha = sys.stdin.readline().strip()
    letras_presentes = set()
    
    for char in linha:
        if char in alfabeto:
            letras_presentes.add(char)
    
    if letras_presentes == alfabeto:
        print('S')
    else:
        print('N')

if __name__ == "__main__":
    main()