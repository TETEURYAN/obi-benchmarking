import sys

input_data = sys.stdin.read().split()
K = int(input_data[0])
N = int(input_data[1])
alfabeto = set(input_data[2:2+K])
mensagem = input_data[2+K:2+K+N]

pode = all(char in alfabeto for char in mensagem)
print('S' if pode else 'N')