
import sys
import random

# Aumentar o limite de recursão para evitar erros de profundidade na árvore
sys.setrecursionlimit(1 << 25)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
    except StopIteration:
        return

    # Estrutura do nó para a Treap Implícita
    class Node:
        __slots__ = ['height', 'prio', 'left', 'right', 'size', 'max_h']
        def __init__(self, height):
            self.height = height
            self.prio = random.randint(1, 1 << 30)
            self.left = None
            self.right = None
            self.size = 1
            self.max_h = height

    def get_size(node):
        return node.size if node else 0

    def get_max(node):
        return node.max_h if node else -1

    def update(node):
        if node:
            node.size = 1 + get_size(node.left) + get_size(node.right)
            node.max_h = max(node.height, get_max(node.left), get_max(node.right))

    def split(node, key):
        # Divide a árvore em duas: esquerda com 'key' nós, direita com o restante
        if not node:
            return (None, None)
        
        current_idx = get_size(node.left)
        if key <= current_idx:
            left, right = split(node.left, key)
            node.left = right
            update(node)
            return (left, node)
        else:
            left, right = split(node.right, key - current_idx - 1)
            node.right = left
            update(node)
            return (node, right)

    def merge(left, right):
        if not left or not right:
            return left or right
        if left.prio > right.prio:
            left.right = merge(left.right, right)
            update(left)
            return left
        else:
            right.left = merge(left, right.left)
            update(right)
            return right

    def query_rightmost(node, val):
        # Encontra o índice (1-based) do nó mais à direita com altura > val
        # Retorna 0 se não encontrar
        if not node or node.max_h <= val:
            return 0
        
        # Priorizar o filho direito (índices maiores)
        if node.right and node.right.max_h > val:
            res = query_rightmost(node.right, val)
            # O índice retornado é relativo ao filho direito, ajustamos
            return get_size(node.left) + 1 + res
        
        # Verificar o nó atual
        if node.height > val:
            return get_size(node.left) + 1
        
        # Se não, buscar no filho esquerdo
        if node.left and node.left.max_h > val:
            return query_rightmost(node.left, val)
        
        return 0

    # Construção inicial da Treap
    root = None
    for _ in range(N):
        h = int(next(iterator))
        root = merge(root, Node(h))
        
    Q = int(next(iterator))
    output = []
    
    for _ in range(Q):
        T = int(next(iterator))
        I = int(next(iterator))
        X = int(next(iterator))
        
        if T == 0:
            # Inserir X atrás do I-ésimo competidor
            # split(root, I) separa os primeiros I elementos (índices 1 a I)
            left, right = split(root, I)
            new_node = Node(X)
            root = merge(merge(left, new_node), right)
        else:
            # Consulta: I-ésima pessoa, parâmetro D = X
            # Dividir em três partes: [1...I-1], [I], [I+1...]
            left, rest = split(root, I - 1)
            mid, right = split(rest, 1)
            
            # mid contém exatamente o nó I
            target_h = mid.height
            threshold = target_h + X
            
            # Buscar na parte esquerda (pessoas à frente na fila)
            res = query_rightmost(left, threshold)
            output.append(str(res))
            
            # Reconstruir a árvore
            root = merge(merge(left, mid), right)
            
    sys.stdout.write('\n'.join(output))

if __name__ == '__main__':
    solve()
