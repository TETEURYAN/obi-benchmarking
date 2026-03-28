k, n = map(int, input().split())
alfabeto = set(input().rstrip('\n'))
mensagem = input().rstrip('\n')

print('S' if all(c in alfabeto for c in mensagem) else 'N')