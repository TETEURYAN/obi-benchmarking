import sys
sys.setrecursionlimit(1_000_000)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    heights = [int(next(it)) for _ in range(N)]
    Q = int(next(it))

    # Árvore de Fenwick (BIT) para alturas máximas em segmentos
    class FenwickMax:
        def __init__(self, n: int):
            self.n = n
            self.bit = [0] * (n + 2)
        def update(self, idx: int, val: int) -> None:
            while idx <= self.n:
                if val > self.bit[idx]:
                    self.bit[idx] = val
                idx += idx & -idx
        def query(self, idx: int) -> int:
            res = 0
            while idx > 0:
                if self.bit[idx] > res:
                    res = self.bit[idx]
                idx -= idx & -idx
            return res

    # Estrutura para armazenar alturas e posições
    # Usaremos uma árvore de segmentos persistente para consultas de máximo em prefixo
    # Mas como há inserções, precisamos de uma estrutura dinâmica.
    # Vamos usar uma árvore de segmentos dinâmica (implicit segment tree) com lazy propagation
    # para alturas máximas em intervalos.
    class Node:
        __slots__ = ('left', 'right', 'max_val')
        def __init__(self):
            self.left = None
            self.right = None
            self.max_val = 0

    class SegTree:
        def __init__(self):
            self.root = Node()
            self.size = 1_000_000_010  # faixa de alturas (1 a 1e9 + delta)
        def _update(self, node: Node, l: int, r: int, idx: int, val: int) -> None:
            if l == r:
                node.max_val = max(node.max_val, val)
                return
            mid = (l + r) // 2
            if idx <= mid:
                if not node.left:
                    node.left = Node()
                self._update(node.left, l, mid, idx, val)
            else:
                if not node.right:
                    node.right = Node()
                self._update(node.right, mid+1, r, idx, val)
            node.max_val = max(node.left.max_val if node.left else 0,
                               node.right.max_val if node.right else 0)
        def update(self, idx: int, val: int) -> None:
            self._update(self.root, 1, self.size, idx, val)
        def _query(self, node: Node, l: int, r: int, ql: int, qr: int) -> int:
            if not node or qr < l or ql > r:
                return 0
            if ql <= l and r <= qr:
                return node.max_val
            mid = (l + r) // 2
            left_res = self._query(node.left, l, mid, ql, qr) if node.left else 0
            right_res = self._query(node.right, mid+1, r, ql, qr) if node.right else 0
            return max(left_res, right_res)
        def query(self, l: int, r: int) -> int:
            return self._query(self.root, 1, self.size, l, r)

    # Lista de alturas na fila (1-indexada)
    arr = [0] + heights  # arr[1..N]
    # Para cada altura, armazenamos a maior posição onde ela aparece
    # Vamos usar uma segtree onde a chave é a altura e o valor é a posição máxima
    seg = SegTree()
    for pos, h in enumerate(arr[1:], 1):
        seg.update(h, pos)

    out_lines = []
    # Processar operações
    for _ in range(Q):
        T = int(next(it))
        I = int(next(it))
        X = int(next(it))
        if T == 0:
            # Inserir nova altura H = X atrás da posição I
            # I pode ser 0 (insere no início)
            pos = I  # posição após a qual inserir (0 = antes do primeiro)
            # Inserir na lista arr
            new_h = X
            new_pos = pos + 1
            arr.insert(new_pos, new_h)
            # Atualizar segtree
            seg.update(new_h, new_pos)
            # Ajustar posições de todos os elementos após new_pos
            # Como segtree armazena por altura, precisamos atualizar todas as alturas afetadas?
            # Na verdade, a segtree armazena a maior posição para cada altura.
            # Se inserimos um elemento, as posições dos elementos à frente aumentam em 1.
            # Isso exigiria atualizar todas as alturas dos elementos à frente.
            # Isso é O(N) por inserção, inviável.
            # Precisamos de uma abordagem diferente.

    # A abordagem acima não é eficiente para inserções.
    # Vamos repensar:
    # Consulta: para a pessoa na posição I, encontrar a pessoa mais próxima à frente
    # com altura > H_I + D.
    # Isso é equivalente a: dado um limite L = H_I + D, encontrar o menor j > I tal que arr[j] > L.
    # Com inserções, precisamos de uma estrutura que suporte:
    #   - Inserção em posição arbitrária
    #   - Consulta de "próximo maior à direita" com limite variável.
    # Podemos usar uma árvore balanceada (ex: treap implícita) que mantém alturas e
    # para cada nó, o máximo na subárvore.
    # Então a consulta pode ser feita em O(log n) percorrendo a árvore.
    # Vamos implementar uma treap implícita.

    import random
    random.seed(0)

    class TreapNode:
        __slots__ = ('priority', 'height', 'max_height', 'size', 'left', 'right')
        def __init__(self, height: int):
            self.priority = random.random()
            self.height = height
            self.max_height = height
            self.size = 1
            self.left = None
            self.right = None

    def update(node: TreapNode) -> None:
        if not node:
            return
        node.size = 1
        node.max_height = node.height
        if node.left:
            node.size += node.left.size
            if node.left.max_height > node.max_height:
                node.max_height = node.left.max_height
        if node.right:
            node.size += node.right.size
            if node.right.max_height > node.max_height:
                node.max_height = node.right.max_height

    def split(node: TreapNode, key: int) -> tuple:
        if not node:
            return (None, None)
        left_size = node.left.size if node.left else 0
        if key <= left_size:
            left, right = split(node.left, key)
            node.left = right
            update(node)
            return (left, node)
        else:
            left, right = split(node.right, key - left_size - 1)
            node.right = left
            update(node)
            return (node, right)

    def merge(left: TreapNode, right: TreapNode) -> TreapNode:
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

    # Construir treap inicial
    root = None
    for h in heights:
        root = merge(root, TreapNode(h))

    # Processar operações
    for _ in range(Q):
        T = int(next(it))
        I = int(next(it))
        X = int(next(it))
        if T == 0:
            # Inserir altura X atrás da posição I (I de 0 a tamanho atual)
            # Na treap implícita, as posições são 0-indexadas.
            # I é a posição após a qual inserir (0 = antes do primeiro)
            # Ou seja, inserir na posição I (0-indexed).
            new_node = TreapNode(X)
            left, right = split(root, I)
            root = merge(merge(left, new_node), right)
        else:
            # Consulta: I é 1-indexed? No enunciado, I-ésimo competidor na fila.
            # Nas operações, I é a posição na fila (1-indexed).
            # Na treap, usamos 0-indexed.
            pos = I - 1  # converter para 0-indexed
            D = X
            # Obter altura da pessoa na posição pos
            # Precisamos percorrer a treap para obter a altura na posição pos.
            # Função auxiliar para obter altura por posição
            def get_height(node: TreapNode, idx: int) -> int:
                if not node:
                    return 0
                left_size = node.left.size if node.left else 0
                if idx < left_size:
                    return get_height(node.left, idx)
                elif idx == left_size:
                    return node.height
                else:
                    return get_height(node.right, idx - left_size - 1)
            H_i = get_height(root, pos)
            limit = H_i + D
            # Agora, precisamos encontrar a menor posição j > pos tal que arr[j] > limit.
            # Podemos fazer uma busca na treap.
            # Função para encontrar a primeira posição à direita com altura > limit.
            def find_first_greater(node: TreapNode, start_pos: int, current_pos: int, limit: int) -> int:
                # current_pos é a posição do primeiro elemento na subárvore 'node' no array global.
                if not node or node.max_height <= limit:
                    return -1  # não encontrado
                left_size = node.left.size if node.left else 0
                # Verificar se há no filho esquerdo
                if node.left and node.left.max_height > limit:
                    return find_first_greater(node.left, start_pos, current_pos, limit)
                # Verificar o nó atual
                node_pos = current_pos + left_size
                if node_pos > start_pos and node.height > limit:
                    return node_pos
                # Verificar filho direito
                if node.right:
                    res = find_first_greater(node.right, start_pos, current_pos + left_size + 1, limit)
                    if res != -1:
                        return res
                return -1

            # Encontrar a primeira posição à direita de pos com altura > limit.
            # A treap root cobre todo o array.
            # Queremos buscar apenas no intervalo [pos+1, n-1].
            # Podemos splitar a treap em [0, pos] e [pos+1, n-1] e buscar na segunda parte.
            left, right = split(root, pos+1)  # left tem [0..pos], right tem [pos+1..]
            if not right:
                ans = 0
            else:
                # Buscar em right a primeira posição com altura > limit.
                # Em right, as posições são deslocadas: a posição 0 em right corresponde a pos+1 no array original.
                found = find_first_greater(right, -1, 0, limit)
                if found == -1:
                    ans = 0
                else:
                    ans = found + (pos + 1) + 1  # converter para 1-indexed
            out_lines.append(str(ans))
            # Reconstruir root
            root = merge(left, right)

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()