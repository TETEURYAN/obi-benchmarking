import sys
import random

# Aumentar o limite de recursão para evitar erros nos casos profundos da Treap
sys.setrecursionlimit(2000000)

# Leitura rápida de entrada
input_data = sys.stdin.read().split()
iterator = iter(input_data)

def next_int():
    return int(next(iterator))

# Estrutura do nó da Treap
class Node:
    __slots__ = ['h', 'prio', 'left', 'right', 'size', 'max_h']
    def __init__(self, h):
        self.h = h
        self.prio = random.getrandbits(30)
        self.left = None
        self.right = None
        self.size = 1
        self.max_h = h

# Função para atualizar os campos agregados (tamanho e altura máxima) de um nó
def update(node):
    if node is None:
        return
    node.size = 1
    node.max_h = node.h
    if node.left:
        node.size += node.left.size
        node.max_h = max(node.max_h, node.left.max_h)
    if node.right:
        node.size += node.right.size
        node.max_h = max(node.max_h, node.right.max_h)

# Função para dividir a Treap em duas árvores: uma com os primeiros k nós e outra com o restante
def split(root, k):
    if root is None:
        return None, None
    
    l_size = root.left.size if root.left else 0
    
    if k <= l_size:
        left, right = split(root.left, k)
        root.left = right
        update(root)
        return left, root
    else:
        left, right = split(root.right, k - l_size - 1)
        root.right = left
        update(root)
        return root, right

# Função para mesclar duas Treaps (todos os nós da esquerda devem ter prioridade implícita menor que os da direita)
def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    
    if left.prio > right.prio:
        left.right = merge(left.right, right)
        update(left)
        return left
    else:
        right.left = merge(left, right.left)
        update(right)
        return right

# Função para encontrar o índice (0-based) do elemento mais à direita com altura > threshold
def query_rightmost(node, threshold):
    if node is None or node.max_h <= threshold:
        return -1
    
    # Priorizar o filho direito para encontrar o elemento mais à direita
    res = query_rightmost(node.right, threshold)
    if res != -1:
        l_size = node.left.size if node.left else 0
        return l_size + 1 + res
    
    # Verificar o nó atual
    if node.h > threshold:
        l_size = node.left.size if node.left else 0
        return l_size
    
    # Se não encontrou à direita nem no atual, buscar à esquerda
    return query_rightmost(node.left, threshold)

def solve():
    try:
        N = next_int()
    except StopIteration:
        return

    root = None
    # Construção inicial da fila
    for _ in range(N):
        h = next_int()
        root = merge(root, Node(h))
        
    Q = next_int()
    results = []
    
    for _ in range(Q):
        T = next_int()
        I = next_int()
        X = next_int()
        
        if T == 0:
            # Operação de inserção: inserir X atrás do I-ésimo (0-indexed I)
            # I é a posição (1-based) do competidor existente. Se I=0, insere no início.
            # A lógica de split(root, I) pega os primeiros I nós (índices 0 a I-1).
            # Isso coloca o novo nó exatamente na posição I (0-based), que é atrás do I-ésimo (1-based).
            left, right = split(root, I)
            new_node = Node(X)
            root = merge(merge(left, new_node), right)
        else:
            # Operação de consulta: I-ésima pessoa (1-based), parâmetro D=X
            # Dividir em: [1...I-1], [I], [I+1...]
            left, right = split(root, I - 1)
            mid, right2 = split(right, 1)
            
            # mid contém exatamente o nó I. Como é uma árvore de tamanho 1, a raiz é o nó.
            h_p = mid.h
            threshold = h_p + X
            
            idx = query_rightmost(left, threshold)
            
            if idx == -1:
                results.append("0")
            else:
                # O índice retornado é 0-based dentro da subárvore 'left'.
                # A posição na fila original é idx + 1 (conversão para 1-based).
                results.append(str(idx + 1))
            
            # Reconstruir a árvore
            root = merge(left, merge(mid, right2))
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()