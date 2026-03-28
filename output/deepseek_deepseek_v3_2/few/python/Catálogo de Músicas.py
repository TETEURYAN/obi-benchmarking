import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    paths = [next(it) for _ in range(n)]
    
    # Construir árvore de prefixos (Trie)
    root = {}
    total_len = 0
    for path in paths:
        parts = path.split('/')
        total_len += len(path)  # comprimento original
        node = root
        for part in parts:
            if part not in node:
                node[part] = {}
            node = node[part]
    
    # DFS para calcular economia máxima
    best_saving = 0
    
    def dfs(node, depth):
        nonlocal best_saving
        # Economia se esta pasta for referência:
        # Para cada arquivo nesta pasta ou subpastas,
        # economizamos depth barras e depth*(nome da pasta) caracteres
        # Mas precisamos adicionar "../" para cada nível acima
        # Na verdade, é mais fácil pensar em:
        # Se escolhermos esta pasta como referência, todos os arquivos
        # nesta subárvore terão seus caminhos reduzidos em depth*(len(part)+1)
        # mas os arquivos fora desta subárvore terão que adicionar 3*depth caracteres
        # por nível (para "../").
        # Vamos calcular de forma diferente:
        # Para cada nó, calcular o número de arquivos na sua subárvore
        file_count = 0
        total_len_in_subtree = 0
        
        # Percorrer subárvore
        stack = [(node, depth)]
        while stack:
            cur_node, cur_depth = stack.pop()
            # Se é um nó folha (não tem filhos), representa um arquivo?
            # Na verdade, o último componente do caminho é o arquivo.
            # Vamos marcar arquivos durante a construção.
            # Modificação: durante a construção, marcar os finais de caminho
            pass
        
        # Abordagem alternativa: calcular para cada pasta a economia líquida
        # Economia = soma sobre todos os arquivos na subárvore de (depth*(len(part)+1))
        #            - soma sobre todos os arquivos fora da subárvore de (3*depth)
        # Mas número de arquivos fora = n - files_in_subtree
        # Então economia = depth * [ soma(len(part)+1 para arquivos na subárvore) - 3*(n - files_in_subtree) ]
    
    # Vamos usar uma abordagem mais direta:
    # Para cada pasta possível (nós internos da árvore), calcular o comprimento total
    # do catálogo se essa pasta for a referência.
    # Comprimento = soma para cada arquivo de:
    #   se arquivo está na subárvore: len(relative_path)
    #   senão: len('../'*depth + path_from_lca)
    # Isso é O(N^2) se feito ingenuamente.
    
    # Precisamos de uma solução O(N log N) ou O(N).
    # Observação: podemos pensar em termos de economia em relação à raiz.
    # Se a referência é a raiz, comprimento = total_len.
    # Se mudamos a referência para um nó na profundidade d, para cada arquivo:
    #   - se está na subárvore: economiza d*(len(part)+1) caracteres (cada parte do caminho acima)
    #   - se não está: adiciona 3*d caracteres (para "../" em cada nível)
    # Então economia líquida = soma_{arquivo na subárvore} d*(len(part)+1) - soma_{outros} 3*d
    # = d * [ soma_{na subárvore} (len(part)+1) - 3*(n - files_in_subtree) ]
    
    # Precisamos para cada nó:
    # 1. files_in_subtree: número de arquivos na subárvore
    # 2. sum_len_parts: soma dos (len(part)+1) para todos os arquivos na subárvore
    #    onde part são os componentes do caminho ACIMA do nó (não incluindo o próprio nó)
    
    # Reconstruir árvore com contagens
    class Node:
        __slots__ = ('children', 'file_count', 'sum_len', 'depth_sum')
        def __init__(self):
            self.children = {}
            self.file_count = 0  # arquivos nesta pasta (não na subárvore)
            self.sum_len = 0     # soma dos comprimentos dos caminhos dos arquivos nesta pasta
            self.depth_sum = 0   # soma das profundidades dos arquivos na subárvore (para cálculo)
    
    root = Node()
    # Inserir todos os caminhos
    for path in paths:
        parts = path.split('/')
        node = root
        for i, part in enumerate(parts):
            if part not in node.children:
                node.children[part] = Node()
            node = node.children[part]
            if i == len(parts) - 1:  # último componente é o arquivo
                node.file_count += 1
                node.sum_len += len(part)
            else:
                # Para pastas intermediárias, o comprimento inclui a barra
                node.sum_len += len(part) + 1
    
    # Agora fazer DFS para calcular para cada nó:
    # total_files_in_subtree: total de arquivos na subárvore
    # total_sum_len_in_subtree: soma dos sum_len dos arquivos na subárvore
    # Mas precisamos do sum_len apenas dos componentes ACIMA do nó atual.
    # Vamos recalcular: para cada arquivo, sua contribuição para um nó ancestral
    # é o comprimento do caminho do nó até o arquivo.
    
    # Melhor abordagem: para cada arquivo, seu caminho completo tem comprimento L.
    # Se a referência está na profundidade d, e o arquivo está na subárvore,
    # o novo caminho tem comprimento L - (comprimento do prefixo até a referência).
    # O comprimento do prefixo é soma_{part in prefix} (len(part)+1).
    # Vamos pré-computar para cada arquivo seu caminho e comprimento.
    
    # Vamos construir uma lista de tuplas (caminho como lista de partes, comprimento_total)
    files = []
    for path in paths:
        parts = path.split('/')
        files.append((parts, len(path)))
    
    # Construir árvore de prefixos com IDs
    node_id = 0
    node_info = []  # lista de dicts com children, parent, depth, path_len_to_node
    root_id = node_id
    node_info.append({'children': {}, 'parent': -1, 'depth': 0, 'path_len': 0, 'file_count': 0})
    node_id += 1
    
    # Mapeamento de (node, part) para id
    def get_or_create_node(parent_id, part):
        nonlocal node_id
        children = node_info[parent_id]['children']
        if part in children:
            return children[part]
        new_id = node_id
        node_info.append({
            'children': {},
            'parent': parent_id,
            'depth': node_info[parent_id]['depth'] + 1,
            'path_len': node_info[parent_id]['path_len'] + len(part) + (1 if parent_id != root_id else 0),
            'file_count': 0
        })
        node_id += 1
        children[part] = new_id
        return new_id
    
    # Inserir todos os caminhos
    file_nodes = []
    for parts in [f[0] for f in files]:
        current = root_id
        for i, part in enumerate(parts):
            if i == len(parts) - 1:  # arquivo
                node_info[current]['file_count'] += 1
                file_nodes.append(current)
            else:  # pasta
                current = get_or_create_node(current, part)
    
    # Agora para cada nó, calcular:
    # files_in_subtree: número de arquivos na subárvore
    # sum_path_len_in_subtree: soma dos comprimentos dos caminhos dos arquivos na subárvore
    # Mas precisamos do comprimento do prefixo comum.
    
    # Fazer DFS pós-ordem para calcular files_in_subtree
    def dfs_count(node):
        total_files = node_info[node]['file_count']
        total_len = 0
        for child in node_info[node]['children'].values():
            child_files, child_len = dfs_count(child)
            total_files += child_files
            total_len += child_len
        node_info[node]['subtree_files'] = total_files
        node_info[node]['subtree_len'] = total_len
        return total_files, total_len
    
    dfs_count(root_id)
    
    # Agora calcular economia para cada nó
    total_len_root = sum(f[1] for f in files)
    best = total_len_root
    
    def dfs_economy(node):
        nonlocal best
        # Economia se este nó for referência:
        # Para cada arquivo na subárvore: economiza node_info[node]['path_len']
        # Para cada arquivo fora: adiciona 3 * node_info[node]['depth']
        files_in = node_info[node]['subtree_files']
        files_out = n - files_in
        economy = files_in * node_info[node]['path_len'] - files_out * (3 * node_info[node]['depth'])
        new_len = total_len_root - economy
        if new_len < best:
            best = new_len
        
        for child in node_info[node]['children'].values():
            dfs_economy(child)
    
    dfs_economy(root_id)
    
    print(best)

if __name__ == "__main__":
    solve()