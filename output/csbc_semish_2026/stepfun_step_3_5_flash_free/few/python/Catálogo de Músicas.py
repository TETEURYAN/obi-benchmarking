import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    caminhos = data[1:1+n]
    
    Total0 = 0
    nodes = [{'pai': -1, 'filhos': {}, 'prof': 0, 'L': 0, 'arquivos_diretos': 0, 'cnt': 0}]
    
    for caminho in caminhos:
        Total0 += len(caminho)
        partes = caminho.split('/')
        pastas = partes[:-1]
        no = 0
        for pasta in pastas:
            if pasta not in nodes[no]['filhos']:
                idx = len(nodes)
                nodes.append({
                    'pai': no,
                    'filhos': {},
                    'prof': nodes[no]['prof'] + 1,
                    'L': nodes[no]['L'] + len(pasta),
                    'arquivos_diretos': 0,
                    'cnt': 0
                })
                nodes[no]['filhos'][pasta] = idx
            no = nodes[no]['filhos'][pasta]
        nodes[no]['arquivos_diretos'] += 1
    
    sys.setrecursionlimit(300000)
    def dfs_cnt(no):
        total = nodes[no]['arquivos_diretos']
        for filho in nodes[no]['filhos'].values():
            total += dfs_cnt(filho)
        nodes[no]['cnt'] = total
        return total
    dfs_cnt(0)
    
    def dfs_dp(no):
        W_no = nodes[no]['L'] + 4 * nodes[no]['prof']
        if no == 0:
            dp = W_no * nodes[no]['cnt']
        else:
            pai = nodes[no]['pai']
            W_pai = nodes[pai]['L'] + 4 * nodes[pai]['prof']
            dp = nodes[pai]['dp'] + nodes[no]['cnt'] * (W_no - W_pai)
        nodes[no]['dp'] = dp
        for filho in nodes[no]['filhos'].values():
            dfs_dp(filho)
    dfs_dp(0)
    
    min_total = None
    for no in range(len(nodes)):
        prof = nodes[no]['prof']
        total_no = 3 * n * prof + Total0 - nodes[no]['dp']
        if min_total is None or total_no < min_total:
            min_total = total_no
    
    print(min_total)

if __name__ == '__main__':
    main()