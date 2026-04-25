
import sys
import bisect

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    
    N = int(next(it))
    heights = [int(next(it)) for _ in range(N)]
    Q = int(next(it))
    
    # Estrutura para consultas: lista de alturas e lista de índices originais
    # Usaremos uma árvore de Fenwick (BIT) para manter alturas máximas em intervalos
    # Mas como há inserções, precisamos de uma estrutura dinâmica
    # Vamos usar uma árvore de segmentos dinâmica (coordenadas compressadas)
    
    # Primeiro coletamos todas as alturas iniciais e das operações tipo 0
    all_heights = []
    ops = []
    for _ in range(Q):
        T = int(next(it))
        I = int(next(it))
        X = int(next(it))
        ops.append((T, I, X))
        if T == 0:
            all_heights.append(X)
    
    # Adiciona alturas iniciais
    all_heights.extend(heights)
    
    # Compressão de coordenadas
    sorted_heights = sorted(set(all_heights))
    height_to_idx = {h: i+1 for i, h in enumerate(sorted_heights)}
    m = len(sorted_heights)
    
    # BIT para máximo
    class BITMax:
        def __init__(self, n):
            self.n = n
            self.tree = [0]*(n+2)
        
        def update(self, idx, val):
            while idx <= self.n:
                if val > self.tree[idx]:
                    self.tree[idx] = val
                idx += idx & -idx
        
        def query(self, idx):
            res = 0
            while idx > 0:
                if self.tree[idx] > res:
                    res = self.tree[idx]
                idx -= idx & -idx
            return res
    
    bit = BITMax(m)
    
    # Lista para manter a fila
    # Vamos usar uma lista Python normal e fazer inserções O(n) - não vai passar
    # Precisamos de uma estrutura de dados que suporte inserção e acesso por índice em O(log n)
    # Vamos usar uma árvore binária balanceada (treap)
    
    import random
    random.seed(42)
    
    class Node:
        __slots__ = ('height', 'height_idx', 'size', 'priority', 'left', 'right', 'max_height_idx')
        def __init__(self, height, height_idx):
            self.height = height
            self.height_idx = height_idx
            self.size = 1
            self.priority = random.random()
            self.left = None
            self.right = None
            self.max_height_idx = height_idx
    
    def update(node):
        if node:
            node.size = 1 + size(node.left) + size(node.right)
            node.max_height_idx = node.height_idx
            if node.left and node.left.max_height_idx > node.max_height_idx:
                node.max_height_idx = node.left.max_height_idx
            if node.right and node.right.max_height_idx > node.max_height_idx:
                node.max_height_idx = node.right.max_height_idx
    
    def size(node):
        return node.size if node else 0
    
    def split(node, key):
        if not node:
            return (None, None)
        if size(node.left) >= key:
            left, right = split(node.left, key)
            node.left = right
            update(node)
            return (left, node)
        else:
            left, right = split(node.right, key - size(node.left) - 1)
            node.right = left
            update(node)
            return (node, right)
    
    def merge(left, right):
        if not left or not right:
            return left or right
        if left.priority > right.priority:
            left.right = merge(left.right, right)
            update(left)
            return left
        else:
            right.left = merge(left, right.left)
            update(right)
            return right
    
    def insert_at(root, pos, node):
        left, right = split(root, pos)
        return merge(merge(left, node), right)
    
    def get_height_at(root, pos):
        if not root:
            return 0
        left_size = size(root.left)
        if pos < left_size:
            return get_height_at(root.left, pos)
        elif pos == left_size:
            return root.height
        else:
            return get_height_at(root.right, pos - left_size - 1)
    
    def get_height_idx_at(root, pos):
        if not root:
            return 0
        left_size = size(root.left)
        if pos < left_size:
            return get_height_idx_at(root.left, pos)
        elif pos == left_size:
            return root.height_idx
        else:
            return get_height_idx_at(root.right, pos - left_size - 1)
    
    def find_first_greater(root, start_pos, min_height_idx):
        # Encontra a primeira posição >= start_pos com height_idx > min_height_idx
        # Retorna posição (0-indexed) ou -1 se não encontrar
        node = root
        pos = start_pos
        result = -1
        
        while node:
            left_size = size(node.left)
            current_pos = pos + left_size
            
            # Verifica se há algum à direita que satisfaz
            if node.right and node.right.max_height_idx > min_height_idx:
                # Vai para a direita
                node = node.right
                pos = current_pos + 1
            elif node.height_idx > min_height_idx:
                # O nó atual satisfaz
                result = current_pos
                # Tenta encontrar um mais à esquerda
                if node.left and node.left.max_height_idx > min_height_idx:
                    node = node.left
                else:
                    break
            else:
                # Nó atual não satisfaz, vai para a esquerda
                if node.left and node.left.max_height_idx > min_height_idx:
                    node = node.left
                else:
                    break
        
        return result
    
    # Inicializa a treap com alturas iniciais
    root = None
    for i, h in enumerate(heights):
        idx = height_to_idx[h]
        node = Node(h, idx)
        root = insert_at(root, i, node)
        bit.update(idx, i+1)  # +1 para 1-indexed
    
    out_lines = []
    total_people = N
    
    for T, I, X in ops:
        if T == 0:
            # Inserir nova pessoa
            h = X
            idx = height_to_idx[h]
            node = Node(h, idx)
            root = insert_at(root, I, node)
            total_people += 1
            
            # Atualiza BIT - precisa atualizar para todas as posições >= I
            # Mas BIT não suporta atualização de intervalo para máximo eficientemente
            # Vamos usar uma abordagem diferente para consultas
            
        else:
            # Consulta
            D = X
            pos = I - 1  # 0-indexed
            
            if pos >= total_people:
                out_lines.append("0")
                continue
            
            h_i = get_height_at(root, pos)
            target_height = h_i + D
            
            # Encontra o menor índice de altura > target_height
            target_idx = bisect.bisect_right(sorted_heights, target_height)
            if target_idx >= m:
                out_lines.append("0")
                continue
            
            min_height_idx = target_idx + 1  # +1 porque height_to_idx é 1-indexed
            
            # Encontra a primeira pessoa à frente com altura suficiente
            result_pos = find_first_greater(root, pos + 1, min_height_idx)
            
            if result_pos == -1:
                out_lines.append("0")
            else:
                out_lines.append(str(result_pos + 1))  # +1 para 1-indexed
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
