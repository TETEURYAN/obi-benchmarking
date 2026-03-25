import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
paths = input_data[1:N+1]

# tree armazena os nós das pastas. 
# Cada nó é uma lista: [tamanho_do_nome, quantidade_de_arquivos_na_subarvore, dicionario_de_filhos]
# O índice 0 é a raiz.
tree = [[0, 0, {}]]

total_root_ans = 0

for path in paths:
    total_root_ans += len(path)
    parts = path.split('/')
    curr = 0
    tree[0][1] += 1
    
    # O último elemento de parts é o arquivo, os anteriores são pastas
    for i in range(len(parts) - 1):
        folder = parts[i]
        if folder not in tree[curr][2]:
            tree.append([len(folder), 0, {}])
            tree[curr][2][folder] = len(tree) - 1
        curr = tree[curr][2][folder]
        tree[curr][1] += 1

min_ans = total_root_ans

# DFS iterativa para evitar o limite de recursão
stack = [(0, total_root_ans)]

while stack:
    u, current_ans = stack.pop()
    if current_ans < min_ans:
        min_ans = current_ans
    
    for v in tree[u][2].values():
        child_length = tree[v][0]
        child_files = tree[v][1]
        
        # Se movermos a referência para a pasta filha:
        # - Para os arquivos fora da subárvore da filha, adicionamos '../' (3 caracteres)
        # - Para os arquivos dentro da subárvore da filha, removemos 'nome_da_pasta/' (child_length + 1 caracteres)
        change = 3 * (N - child_files) - (child_length + 1) * child_files
        
        stack.append((v, current_ans + change))

print(min_ans)