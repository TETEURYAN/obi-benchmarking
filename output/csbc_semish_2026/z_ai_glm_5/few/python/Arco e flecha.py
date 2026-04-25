import sys
import random

# Aumentar o limite de recursão para evitar erros em árvores profundas (embora a probabilidade seja baixa com Treap)
sys.setrecursionlimit(200000)

# Leitura rápida de toda a entrada
input_data = sys.stdin.read().split()

if not input_data:
    exit()

iterator = iter(input_data)

# Definição da classe Node para a Treap (Árvore Binária de Busca Aleatorizada)
class Node:
    __slots__ = ['val', 'prio', 'left', 'right', 'size', 'count']
    def __init__(self, val):
        self.val = val
        self.prio = random.random()
        self.left = None
        self.right = None
        self.size = 1
        self.count = 1

def get_size(node):
    return node.size if node else 0

def update_size(node):
    if node:
        node.size = node.count + get_size(node.left) + get_size(node.right)

# Divide a árvore em duas: uma com valores <= key e outra com valores > key
def split(node, key):
    if not node:
        return (None, None)
    if node.val <= key:
        left_sub, right_sub = split(node.right, key)
        node.right = left_sub
        update_size(node)
        return (node, right_sub)
    else:
        left_sub, right_sub = split(node.left, key)
        node.left = right_sub
        update_size(node)
        return (left_sub, node)

# Mescla duas árvores (todos os valores da esquerda < valores da direita)
def merge(left, right):
    if not left or not right:
        return left or right
    if left.prio > right.prio:
        left.right = merge(left.right, right)
        update_size(left)
        return left
    else:
        right.left = merge(left, right.left)
        update_size(right)
        return right

# Insere um valor na Treap
def insert(root, val):
    # Divide em menores/iguais e maiores
    l, r = split(root, val)
    # Divide a parte dos menores/iguais para isolar os iguais a val
    l, mid = split(l, val - 1)
    
    if mid:
        # Se o valor já existe, incrementa o contador
        mid.count += 1
        update_size(mid)
    else:
        # Se não existe, cria novo nó
        mid = Node(val)
    
    # Mescla de volta: (menores) + (val) + (maiores)
    return merge(merge(l, mid), r)

# Conta quantos elementos são menores ou iguais a val
def count_leq(node, val):
    count = 0
    while node:
        if node.val <= val:
            count += get_size(node.left) + node.count
            node = node.right
        else:
            node = node.left
    return count

# Processamento principal
try:
    n_str = next(iterator)
    n = int(n_str)
except StopIteration:
    exit()

root = None
prev_penalty = 0
output = []

for _ in range(n):
    try:
        x_in = int(next(iterator))
        y_in = int(next(iterator))
    except StopIteration:
        break
    
    # Calcula coordenadas reais
    x_real = x_in + prev_penalty
    y_real = y_in + prev_penalty
    
    # Calcula distância quadrada
    dist_sq = x_real * x_real + y_real * y_real
    
    # Calcula penalidade atual (número de flechas anteriores com distância <= dist_sq)
    current_penalty = count_leq(root, dist_sq)
    output.append(str(current_penalty))
    
    # Insere a flecha atual na estrutura de dados
    root = insert(root, dist_sq)
    
    # Atualiza a penalidade para a próxima iteração
    prev_penalty = current_penalty

# Imprime a saída formatada
sys.stdout.write('\n'.join(output) + '\n')